import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

import Header from "@/components/Header";
import Footer from "@/components/Footer";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "이예니 | 주니어 개발자 포트폴리오",
  description: "Next.js와 Tailwind CSS로 제작한 포트폴리오 사이트입니다.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body
        className={`
          ${geistSans.variable} ${geistMono.variable} antialiased
          flex flex-col min-h-screen
        `}
      >
        <Header />

        <main className="flex flex-1 justify-center items-center bg-[#FAFAFA]">
          {children}
        </main>
        
        <Footer />

      </body>
    </html>
  );
}
