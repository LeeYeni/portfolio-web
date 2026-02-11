"use client"

import { useState, useEffect, useRef } from "react";
import ChatBubble from "@/components/ChatBubble";
import ChatInput from "@/components/ChatInput";
import { startChat, getChatbotResponse } from "@/api/chatbot";

interface Message {
    id: number;
    text: string;
    sender: "user" | "bot"
}

export default function ChatbotPage() {
    // localStorage.clear();
    const [messages, setMessages] = useState<Message[]>([]);
    const [sessionId, setSessionId] = useState<string | null>(null);
    const scrollRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const initChat = async () => {
            let sid = localStorage.getItem("session_id");
            let welcomeMsg = "";

            if (sid) {
                welcomeMsg = "다시 오셨군요! 궁금한 점이 있으시면 언제든 물어봐 주세요. ✨"
            } else {
                const data = await startChat();
                sid = data.session_id;
                welcomeMsg = data.message;
                localStorage.setItem("session_id", sid);
            }

            setSessionId(sid);

            const welcomeMessage: Message = {
                id: Date.now(),
                text: welcomeMsg,
                sender: "bot"
            };
            setMessages([welcomeMessage]);
        };
        initChat();
    }, []);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTo({
                top: scrollRef.current.scrollHeight,
                behavior: "smooth",
            });
        }
    }, [messages]);

    const handleSendMessage = async (text: string) => {
        if (!sessionId) return;
        
        const userMessage: Message = {
            id: Date.now(),
            text: text,
            sender: "user"
        };

        setMessages((prev) => [...prev, userMessage]);

        const response = await getChatbotResponse(sessionId, text);

        const botMessage: Message = {
            id: Date.now(),
            text: response.message,
            sender: "bot"
        }

        setMessages((prev) => [...prev, botMessage]);
    };

    return (
        <div className="fixed z-0 w-full top-16 h-135 px-4 flex flex-col">
            <div
                ref={scrollRef}
                className="flex-1 overflow-y-auto flex flex-col py-4 gap-4"
            >
                {messages.map((message) => (
                    <ChatBubble key={message.id} content={message.text} sender={message.sender} />
                ))}
            </div>

            <div className="bg-[#FAFAFA]">
                <ChatInput onSendMessage={handleSendMessage} placeholder="챗봇에게 물어보기" chatbot />
            </div>
        </div>
    )
}