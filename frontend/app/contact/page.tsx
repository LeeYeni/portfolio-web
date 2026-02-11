"use client"

import { useState } from "react";
import { Mail, Tag, Send } from "lucide-react";
import ContactInput from "@/components/ContactInput";
import { sendEmail } from "@/api/email";

export default function MailSenderCard() {
    const [formData, setFormData] = useState({
        organization: "",
        email: "",
    });

    const [isSubmitting, setIsSubmitting] = useState(false);

    const handleInputChange = (field: string, value: string) => {
        setFormData((prev) => ({
            ...prev,
            [field]: value
        }));
    };

    const handleSendMail = async () => {
        const { organization, email } = formData;

        // 간단한 유효성 검사
        if (!organization || !email) {
            alert("회사명과 이메일을 모두 입력해주세요.");
            return;
        }

        // 이메일 형식 체크
        if (!email.includes("@")) {
            alert("올바른 이메일 형식을 입력해주세요.");
            return;
        }

        setIsSubmitting(true);
        try {
            const response = await sendEmail(organization, email);
            alert("성공적으로 포트폴리오 요약본이 도착했습니다."); // "성공적으로 메일을 전송했습니다."
            // 성공 시 입력창 초기화
            setFormData({ organization: "", email: "" });
        } catch (error) {
            console.error(error);
            alert("메일 전송 중 오류가 발생했습니다. 다시 시도해주세요.");
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <div className="fixed top-16 p-4 flex flex-col w-full gap-4">
            <div className="flex flex-col gap-4">
                <ContactInput
                    label="회사명"
                    placeholder="회사명을 입력해주세요"
                    value={formData.organization}
                    onChange={(value) => handleInputChange("organization", value)}
                    icon={Tag}
                />

                <ContactInput
                    label="이메일"
                    placeholder="이메일 주소를 입력해주세요"
                    value={formData.email}
                    onChange={(value) => handleInputChange("email", value)}
                    icon={Mail}
                />
            </div>

            <div className="flex flex-col items-center gap-3">
                <div className="text-xs text-gray-500 py-2">
                    회사명, 이메일만 입력하면 포트폴리오 요약본을 전송해줘요!
                </div>

                {/* 전송 버튼 */}
                <button
                    onClick={handleSendMail}
                    disabled={isSubmitting}
                    className={`w-full max-w-xs flex items-center justify-center gap-2 py-3 px-6 rounded-xl font-medium transition-all
                        ${isSubmitting 
                            ? "bg-gray-200 text-gray-400 cursor-not-allowed" 
                            : "bg-blue-600 text-white hover:bg-blue-700 active:scale-95 shadow-md"
                        }`}
                >
                    {isSubmitting ? (
                        "전송 중..."
                    ) : (
                        <>
                            <Send size={18} />
                            <span>포트폴리오 받기</span>
                        </>
                    )}
                </button>
            </div>
        </div>
    )
}