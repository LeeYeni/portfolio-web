"use client"

import { useState } from "react";
import { usePathname } from "next/navigation";
import { Github, Linkedin, ExternalLink, Share2, X } from "lucide-react";
import SocialLink from "./SocialLink";

export default function Footer() {
    const [isVisible, setIsVisible] = useState(false);

    const pathname = usePathname();
    const hiddenPaths = ["/chatbot", "/guestbook", "/contact"]

    if (hiddenPaths.includes(pathname)) return null;

    return (
        <div className="fixed bottom-8 right-8 flex flex-col-reverse p-4">
            <button
              onClick={() => setIsVisible(!isVisible)}
              className="flex flex-row gap-2 rounded-2xl px-4 py-2 hover:text-[#15d3fe] shadow-lg transition-all"
            >
                {isVisible ? (
                    <X />
                ) : (
                    <Share2 />
                )}
                <span>{isVisible ? "CLOSE": "CONTACT"}</span>
            </button>

            {isVisible && (
                <footer>
                    <SocialLink
                        href="https://github.com/LeeYeni"
                        icon={Github}
                        label="Github"
                    />

                    <SocialLink
                        href="https://blog.naver.com/twoyen2"
                        icon={ExternalLink}
                        label="Blog"
                    />

                    <SocialLink
                        href="https://www.linkedin.com/in/leeyeni/"
                        icon={Linkedin}
                        label="LinkedIn"
                    />
                </footer>
            )}
        </div>
    )
}