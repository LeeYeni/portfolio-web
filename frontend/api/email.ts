export interface EmailRequest {
    organization: string;
    email: string;
}

export interface EmailResponse {
    message: string;
}

// 이메일 전송 요청 (POST /api/email/)
export const sendEmail = async (organization: string, email: string): Promise<EmailResponse> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    const response = await fetch(`${baseUrl}/api/email/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            organization,
            email,
        }),
    });

    if (!response.ok) throw new Error('메일 전송에 실패했습니다.');

    return response.json() as Promise<EmailResponse>;
}