"use client"

import { useEffect, useState } from "react";
import ActionButton from "@/components/ActionButton";
import { createNickname } from "@/api/guest";

export default function Home() {
  const [nickname, setNickname] = useState<string | null>(null);

  useEffect(() => {
    const initializeUser = async () => {
      // 1. localStorage에서 기존 유저 정보 확인
      const savedUuid = localStorage.getItem("guest_uuid");
      const savedNickname = localStorage.getItem("guest_nickname");

      if (savedUuid && savedNickname) {
        setNickname(savedNickname);
        return;
      }

      // 2. 데이터가 없으면 새로운 닉네임 생성
      try {
        const data = await createNickname();
        localStorage.setItem("guest_uuid", data.uuid);
        localStorage.setItem("guest_nickname", data.nickname);
        setNickname(data.nickname);
      } catch (error) {
        console.error("사용자 초기화 에러:", error);
      }
    };

    initializeUser();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center gap-4">
      {/* 닉네임 표시 영역 */}
      {nickname && (
        <div className="mb-4 text-sm text-gray-600 animate-fade-in">
          반가워요, <span className="font-bold text-blue-600">{nickname}</span> 님!
        </div>
      )}
      
      <ActionButton
        label="1분 자기소개 영상 보기 →"
        href="https://yeni-lab.org"
      />

      <ActionButton
        label="노션 이력서 보기 →"
        href="https://yeni-lab.org"
      />

      <ActionButton
        label="챗봇에게 물어보기 →"
        href="/chatbot"
      />
    </div>
  )
}