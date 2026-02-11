import { X } from "lucide-react"
import Link from "next/link"

interface ClosedMenuProps {
    toggleMenu: () => void;
}

export default function MenuOverlay({ toggleMenu }: ClosedMenuProps) {
    return (
        <div className="fixed z-10 inset-0 bg-[#fecf15] text-black font-semibold">
            <header className="flex flex-row sticky top-0 z-50 w-full h-14 p-2 justify-center items-center text-black">
                <button
                    onClick={toggleMenu}
                    className="absolute left-4 transition-opacity cursor-pointer"
                >
                    <X className="font-semibold hover:text-[#15d3fe]"/>
                </button>
                <div className="font-semibold">
                    MENU
                </div>
            </header>

            <main className="flex flex-col gap-8 p-16">
                <Link
                    href="/"
                    onClick={toggleMenu}
                    className="hover:text-[#15d3fe]"
                >
                    01. HOME
                </Link>

                <Link
                    href="/profile"
                    onClick={toggleMenu}
                    className="hover:text-[#15d3fe]"
                >
                    02. ABOUT ME
                </Link>

                <Link
                    href="/project"
                    onClick={toggleMenu}
                    className="hover:text-[#15d3fe]"
                >
                    03. PROJECT
                </Link>

                <Link
                    href="/chatbot"
                    onClick={toggleMenu}
                    className="hover:text-[#15d3fe]"
                >
                    04. CHATBOT
                </Link>

                <Link
                    href="/guestbook"
                    onClick={toggleMenu}
                    className="hover:text-[#15d3fe]"
                >
                    05. GUESTBOOK
                </Link>

                <Link
                    href="/contact"
                    onClick={toggleMenu}
                    className="hover:text-[#15d3fe]"
                >
                    06. CONTACT
                </Link>
            </main>
        </div>
    )
}