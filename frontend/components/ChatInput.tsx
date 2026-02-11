"use client"

import { useState, useRef, useEffect } from "react";
import { Plus, SendHorizontal } from 'lucide-react'; // 아이콘 라이브러리 예시 (Lucide)

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  placeholder: string;
  chatbot: boolean;
}

export default function ChatInput({ onSendMessage, placeholder, chatbot }: ChatInputProps) {
  const [inputValue, setInputValue] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSend = () => {
    if (inputValue.trim() === "") return;  // 빈 메시지는 전송 안 함

    onSendMessage(inputValue);  // 부모로부터 받은 함수 실행
    setInputValue("");  // 입력창 초기화
  };

  // Enter 키 지원
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.nativeEvent.isComposing) return;

    if (e.key === "Enter") {
      if (e.shiftKey) {
        return;
      } else {
        e.preventDefault();  // Enter의 기본 줄바꿈 동작 방지
        handleSend();
      }
    }
  };

  const MAX_HEIGHT = 168;  // 24px * 7줄 기준

  useEffect(() => {
    const textarea = textareaRef.current;

    if (textarea) {
      textarea.style.height = "auto"  // 높이 초기화
      const nextHeight = textarea.scrollHeight;

      if (nextHeight <= MAX_HEIGHT) {
        textarea.style.height = `${nextHeight}px`;
        textarea.style.overflowY = "hidden";
      } else {
        textarea.style.height = `${MAX_HEIGHT}px`;
        textarea.style.overflowY = "auto";
      }
    }
  }, [inputValue]);

  return (
    <div className="fixed z-10 bottom-0 left-0 w-full px-4 py-2 bg-[#FAFAFA]">
        <div className="flex flex-col p-4 gap-4 w-full rounded-2xl border-2 border-[#0f0f0f10] shadow-xs shadow-gray-400/50">
            <textarea
                ref={textareaRef}
                rows={1}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={placeholder}
                className="outline-none placeholder:text-gray-400"
                style={{ minHeight: "24px", overflow: "hidden" }}
            />

            <div className="flex flex-row items-center justify-between">
                <button
                    className="hover:text-[#15d3fe]"
                >
                  <Plus />
                </button>

                <button
                    onClick={handleSend}
                    className="p-2 bg-gray-200 rounded-full hover:bg-[#15d3fe]"
                >
                  <SendHorizontal />
                </button>
            </div>
        </div>

        {chatbot && (
            <div className="flex justify-center items-center text-xs py-2">
                챗봇은 인물 등에 관한 정보 제공 시 실수를 할 수 있으니 다시 한번 확인해주세요.
            </div>
        )}
    </div>
  );
};