import { LucideIcon } from "lucide-react";

interface ContactInputProps {
    label: string,
    placeholder: string,
    value: string;
    icon: LucideIcon;
    onChange: (val: string) => void;
}

export default function ContactInput({
    label, placeholder, value, onChange, icon: Icon
}: ContactInputProps) {
    return (
        <div className="flex flex-col justify-between gap-2">
            <div className="flex flex-row pl-4 items-center justify-start">
                <Icon />
                <label
                    className="font-semibold px-2 text-sm"
                >
                    {label}
                </label>
            </div>
            

            <input
                type="text"
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder={placeholder}
                className="flex-1 px-4 py-2 bg-[#FAFAFA] border-2 rounded-2xl border-[#0f0f0f10] shadow-xs shadow-gray-400/50 outline-none"
            />
        </div>
    )
}