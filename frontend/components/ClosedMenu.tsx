"use client"

import { Menu } from "lucide-react";
import Link from "next/link";

interface ClosedMenuProps {
    toggleMenu: () => void;
}

export default function ClosedMenu({ toggleMenu }: ClosedMenuProps) {
    return (
        <div>
            {/* 1. <header> 태그 사용 */}
            {/* 2. sticky top-0: 스크롤 내려도 상단에 고정 */}
            <header className="flex flex-row sticky top-0 z-10 w-full h-14 p-2 justify-center items-center text-black">
                <button
                    onClick={toggleMenu}
                    className="absolute left-4 transition-opacity cursor-pointer"
                >
                    <Menu className="hover:text-[#15d3fe]"/>
                </button>

                <Link
                    href="/"
                    className="flex justify-center items-center tracking-tight text-black hover:text-[#15d3fe] font-bold cursor-pointer"
                >
                    이예니 | 포트폴리오
                </Link>
            </header>
        </div>
    )
}