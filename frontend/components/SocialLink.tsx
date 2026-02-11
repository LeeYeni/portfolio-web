import { LucideIcon } from "lucide-react";

interface SocialLinkProps {
    href: string;
    icon: LucideIcon;
    label: string;
}

export default function SocialLink({ href, icon: Icon, label }: SocialLinkProps) {
    return(
        <a
            href={href}
            target="_blank"
            className="flex flex-row gap-2 items-center px-4 py-2 hover:text-[#15d3fe] transition-all"
        >
            <div>
                <Icon />
            </div>
            <div>
                {label}
            </div>
        </a>
    )
}