interface ChatBubbleProps {
    content: string
    sender: "user" | "bot"
}

export default function ChatBubble({ content, sender }: ChatBubbleProps) {
    return (
        <div className={`
            px-4 py-2 text-black 
            ${sender === "user"
                ? "self-end rounded-tr-none bg-[#15d3fe5b] rounded-2xl"
                : "self-start"
            }
        `}>
            {content}
        </div>
    )
}