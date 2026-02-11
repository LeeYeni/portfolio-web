"use client"
import { useState, useEffect } from "react";
import ProjectButton from "@/components/ProjectButton";
import ProjectCard from "@/components/ProjectCard";
import { getProjectsByCategory, ProjectItem } from "@/api/project";

export default function ProjectPage() {
    const [selectedCategory, setSelectedCategory] = useState("Data Engineering");
    const [projects, setProjects] = useState<ProjectItem[]>([]);
    const [isLoading, setIsLoading] = useState(false);
    const [isVisible, setIsVisible] = useState(false);

    const STACK = [
        "DATA Engineering", "AI", "BACKEND", "FULLSTACK"
    ]

    // 카테고리가 변경될 때마다 데이터를 가져오는 useEffect
    useEffect(() => {
        const fetchProjects = async () => {
            setIsLoading(true);
            try {
                const data = await getProjectsByCategory(selectedCategory);
                setProjects(data);
            } catch (error) {
                console.error("프로젝트 로딩 실패:", error);
                setProjects([]); // 에러 시 목록 비우기
            } finally {
                setIsLoading(false);
            }
        };

        fetchProjects();
    }, [selectedCategory]);

    return (
        <div className="fixed w-full top-16 h-full overflow-y-auto">
            <div className="flex flex-col p-10 gap-8 pb-32">
                {/* 카테고리 선택 버튼 목록 */}
                <div className="flex flex-row gap-4 overflow-x-auto pb-2">
                    {STACK.map((s) => (
                        <ProjectButton 
                            key={s} 
                            label={s} 
                            // 현재 선택된 버튼 활성화 상태 표시 (ProjectButton에 active 프롭이 있다고 가정)
                            active={selectedCategory === s}
                            onClick={() => setSelectedCategory(s)} 
                        />
                    ))}
                </div>

                {/* 프로젝트 카드 리스트 영역 */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {isLoading ? (
                        <div className="col-span-full text-center py-10 text-gray-500">
                            로딩 중...
                        </div>
                    ) : projects.length > 0 ? (
                        projects.map((project, index) => (
                            <ProjectCard 
                                key={index}
                                title={project.name}
                                description={project.description}
                                startDate={project.start_date}
                                endDate={project.end_date}
                                notionUrl={project.notion_url}
                                githubUrl={project.github_url}
                            />
                        ))
                    ) : (
                        <div className="col-span-full text-center py-10 text-gray-500">
                            해당 카테고리의 프로젝트가 없습니다.
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}