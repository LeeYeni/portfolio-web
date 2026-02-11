interface ProjectItemProps {
    label: string
}

export default function ProjectItem({ label }: ProjectItemProps) {
    return (
        <div className="p-8 border-4 border-[#fecf15] rounded-2xl">
            {label}
        </div>
    )
}