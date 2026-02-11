interface ProjectButtonProps {
    label: string;
    onClick?: () => void;
}

export default function ProjectButton({ label, onClick }: ProjectButtonProps) {
    return (
        <button
            type="button"
            onClick={onClick}
            className="group px-4 py-2 flex items-center justify-center bg-[#fecf15] hover:bg-[#15d3fe] rounded-2xl font-semibold"
        >
            {label}
        </button>
    )
}