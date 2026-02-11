// 자격 증명(Credential) 인터페이스 정의
export interface CredentialItem {
    category: string;
    name: string;
    description: string;
    issuer: string;
    issued_date: string;
    pdf_url: string;
    notion_url: string;
}

export const getCredentialsByCategory = async (category: string): Promise<CredentialItem[]> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    
    // 경로 변수에 한글이 포함될 수 있으므로 encodeURIComponent를 사용합니다.
    const response = await fetch(`${baseUrl}/api/credential/category/${encodeURIComponent(category)}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    if (!response.ok) {
        throw new Error(`${category} 목록을 불러오는데 실패했습니다.`);
    }

    return response.json() as Promise<CredentialItem[]>;
}