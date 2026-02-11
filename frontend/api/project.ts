// 프로젝트 아이템 인터페이스 정의
export interface ProjectItem {
    category: string;
    name: string;
    description: string;
    start_date: string;
    end_date: string;
    notion_url: string;
    github_url: string;
}

export const getProjectsByCategory = async (category: string): Promise<ProjectItem[]> => {
    const baseUrl = process.env.NEXT_PUBLIC_AI_BASE_URL;
    
    // URL 인코딩을 통해 카테고리에 한글이나 공백이 포함되어도 안전하게 요청합니다.
    const response = await fetch(`${baseUrl}/api/project/category/${encodeURIComponent(category)}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    if (!response.ok) {
        throw new Error(`${category} 카테고리의 프로젝트를 불러오는 데 실패했습니다.`);
    }

    return response.json() as Promise<ProjectItem[]>;
}