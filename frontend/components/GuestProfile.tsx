import { UserRound } from "lucide-react"

interface GuestProfileProps {
    color: string;
    nickname: string;
    message: string;
}

export default function GuestProfile({ color, nickname, message }: GuestProfileProps) {
    return (
        <div className="flex flex-row gap-2">
            <div className="items-start">
                <div className={`${color} p-2 rounded-2xl`}>
                    <UserRound />
                </div>
            </div>

            <div className="flex flex-col">
                <div>
                    {nickname}
                </div>
                <div className="bg-[#15d3fe5b] px-4 py-2 rounded-2xl rounded-tl-none">
                    {message}
                </div>
            </div>
        </div>
    )
}