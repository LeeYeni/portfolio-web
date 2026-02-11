"use client"

import { useState, useEffect } from "react"
import GuestProfile from "@/components/GuestProfile"
import ChatInput from "@/components/ChatInput"
import { getGuestMessages, createNickname, postGuestbook, GuestMessage } from "@/api/guest"

interface Message extends GuestMessage {
    id: number;
    color: string;
}

export default function GuestBookPage() {
    const [messages, setMessages] = useState<Message[]>([]);

    const COLORS = [
        'bg-red-400', 'bg-blue-400', 'bg-green-400', 
        'bg-yellow-400', 'bg-purple-400', 'bg-pink-400'
    ];

    // 1. 초기 로드 시 기존 메시지 목록 가져오기
    useEffect(() => {
        const fetchMessages = async () => {
            try {
                const data = await getGuestMessages();
                console.log(data);
                const formattedMessages = data.map((msg, index) => ({
                    ...msg,
                    id: index, // 또는 Date.parse(msg.created_at)
                    color: COLORS[Math.floor(Math.random() * COLORS.length)]
                }));
                setMessages(formattedMessages);
            } catch (error) {
                console.error("메시지를 불러오는데 실패했습니다:", error);
            }
        };

        fetchMessages();
    }, []);

    // 2. 메시지 전송 및 등록
    const handleSendMessage = async (text: string) => {
        try {
            // A. 닉네임과 UUID 가져오기
            const uuid = localStorage.getItem("guest_uuid");
            const nickname = localStorage.getItem("guest_nickname");

            if (!uuid || !nickname) {
                alert("사용자 정보가 없습니다. 메인 페이지로 이동합니다.");
                window.location.href = "/";
                return;
            }

            // B. 서버에 방명록 등록
            await postGuestbook(uuid, text);

            // C. UI 업데이트용 데이터 생성
            const randomColor = COLORS[Math.floor(Math.random() * COLORS.length)]
            const newMessage: Message = {
                id: Date.now(),
                nickname: nickname,
                message: text,
                created_at: new Date().toISOString(),
                color: randomColor,
            };

            setMessages((prev) => [...prev, newMessage]);
        } catch (error) {
            alert("메시지 전송에 실패했습니다.");
            console.error(error);
        }
    };

    return (
        <div className="w-full">
            <div className="fixed top-16 w-full">
                <div className="flex flex-col gap-2 px-6 w-full">
                    {messages.map((message) => (
                        <GuestProfile
                            key={message.id}
                            color={message.color}
                            nickname={message.nickname}
                            message={message.message}
                        />
                    ))}
                </div>
            </div>

            <div className="fixed bottom-0 py-4">
                <ChatInput onSendMessage={handleSendMessage} placeholder="방문해주셔서 감사합니다. 따뜻한 한 마디를 남겨주세요." chatbot={false}/>
            </div>
        </div>
    )
}