export interface GuestMessage {
    nickname: string;
    message: string;
    created_at: string;
}

export interface GuestbookRequest {
    uuid: string;
    message: string;
}

export interface NicknameResponse {
    uuid: string;
    nickname: string;
}

// 방명록 목록 조회 (GET /api/guest/)
export const getGuestMessages = async (): Promise<GuestMessage[]> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    const response = await fetch(`${baseUrl}/api/guest/`);
    
    if (!response.ok) throw new Error('방명록을 불러오는데 실패했습니다.');
    
    return response.json() as Promise<GuestMessage[]>;
}

// 닉네임 생성 요청 (POST /api/guest/nickname)
export const createNickname = async (): Promise<NicknameResponse> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    const response = await fetch(`${baseUrl}/api/guest/nickname`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    if (!response.ok) throw new Error('닉네임 생성에 실패했습니다.');

    return response.json() as Promise<NicknameResponse>;
}

// 방명록 작성 요청 (POST /api/guest/guestbook)
export const postGuestbook = async (uuid: string, message: string): Promise<void> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    const response = await fetch(`${baseUrl}/api/guest/guestbook`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            uuid,
            message,
        }),
    });

    if (!response.ok) throw new Error('방명록 작성에 실패했습니다.');
}