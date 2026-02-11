import { LucideIcon, SendHorizontal } from "lucide-react";

interface ActionableInputProps {
    label: string,
    placeholder: string,
    value: string;
    icon: LucideIcon;
    onChange: (val: string) => void;
}

export default function ActionableInput({
    label, placeholder, value, onChange, icon: Icon
}: ActionableInputProps) {
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
            
            <div className="flex-1 flex flex-col justify-between p-4 bg-[#FAFAFA] border-2 rounded-2xl border-[#0f0f0f10] shadow-xs shadow-gray-400/50 outline-none">
                <textarea
                    rows={12}
                    value={value}
                    onChange={(e) => onChange(e.target.value)}
                    placeholder={placeholder}
                    className="outline-none"
                    style={{ minHeight: "24px", overflow: "hidden" }}
                />

                <div className="flex flex-row items-center justify-end">
                    <button
                        className="p-2 bg-gray-200 rounded-full hover:bg-[#15d3fe]"
                    >
                      <SendHorizontal />
                    </button>
                </div>
            </div>
        </div>
    )
}