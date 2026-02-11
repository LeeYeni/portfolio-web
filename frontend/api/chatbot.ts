export interface ChatbotResponse {
    session_id: string;
    message: string;
}

// 초기 세션 시작 함수
export const startChat = async (): Promise<ChatbotResponse> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    const response = await fetch(`${baseUrl}/api/chatbot/start`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    return response.json() as Promise<ChatbotResponse>;
}

// 챗봇 대화 요청 함수
export const getChatbotResponse = async(session_id: string, prompt: string): Promise<ChatbotResponse> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;

    const response = await fetch(`${baseUrl}/api/chatbot`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            session_id,
            prompt,
        }),
    });

    return response.json() as Promise<ChatbotResponse>;
}