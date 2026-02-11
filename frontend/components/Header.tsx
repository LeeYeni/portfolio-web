"use client";

import { useState } from "react";
import { X } from "lucide-react";
import OpenedMenu from "@/components/OpenedMenu";
import ClosedMenu from "./ClosedMenu";
import Link from "next/link";

export default function Header() {
    // 메뉴가 열렸는지 닫혔는지 상태 관리 (기본값: false)
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    // 메뉴 열고 닫는 함수
    const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

    return (
        <div className="bg-[#FAFAFA]">
            {isMenuOpen ? (
                <OpenedMenu toggleMenu={toggleMenu} />
            ) : (
                <ClosedMenu toggleMenu={toggleMenu} />
            )}
        </div>
    )
}