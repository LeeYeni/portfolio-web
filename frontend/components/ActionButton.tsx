"use client"

import Link from "next/link"

interface ActionButtonProps {
    label: string;  // 버튼에 들어갈 글자
    href: string;  // 이동할 링크 주소
}

export default function ActionButton({ label, href }: ActionButtonProps) {
    return (
        <Link
            href={href}
            className="flex justify-center items-center bg-[#fecf15] hover:bg-[#15d3fe] text-black font-semibold py-4 px-8 w-70 rounded-2xl hover:opacity-80 transition-opacity cursor-pointer"
        >
            {label}
        </Link>
    )
}