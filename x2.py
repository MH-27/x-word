
def x2():
    import os
    xq = open("x1.txt")
    x = xq.readlines()
    num = len(x)-1
    for i in x :
        openxx = open("x1.txt","a")
        openxx.write(f"!{x[num][:-1]}\n"
                     f"{x[num]}"
                     f"!!{x[num][:-1]}\n"
                     f"@{x[num][:-1]}\n"
                     f"@@{x[num][:-1]}\n"
                     f"#{x[num][:-1]}\n"
                     f"##{x[num][:-1]}\n"
                     f"${x[num][:-1]}\n"
                     f"$${x[num][:-1]}\n"
                     f"%{x[num][:-1]}\n"
                     f"%%{x[num][:-1]}\n"
                     f"^{x[num][:-1]}\n"
                     f"^^{x[num][:-1]}\n"
                     f"&{x[num][:-1]}\n"
                     f"&&{x[num][:-1]}\n"
                     f"*{x[num][:-1]}\n"
                     f"**{x[num][:-1]}\n"
                     f"({x[num][:-1]}\n"
                     f"(({x[num][:-1]}\n"
                     f"){x[num][:-1]}\n"
                     f")){x[num][:-1]}\n"
                     f"(){x[num][:-1]}\n"
                     f"(()){x[num][:-1]}\n"
                     f"-{x[num][:-1]}\n"
                     f"--{x[num][:-1]}\n"
                     f"_{x[num][:-1]}\n"
                     f"__{x[num][:-1]}\n"
                     f"={x[num][:-1]}\n"
                     f"=={x[num][:-1]}\n"
                     f"+{x[num][:-1]}\n"
                     f"++{x[num][:-1]}\n"
                     f".{x[num][:-1]}\n"
                     f"..{x[num][:-1]}\n"
                     f",{x[num][:-1]}\n"
                     f",,{x[num][:-1]}\n"
                     f"{x[num][:-1]}!\n"
                     f"{x[num][:-1]}!!\n"
                     f"{x[num][:-1]}@\n"
                     f"{x[num][:-1]}@@\n"
                     f"{x[num][:-1]}#\n"
                     f"{x[num][:-1]}##\n"
                     f"{x[num][:-1]}$\n"
                     f"{x[num][:-1]}$$\n"
                     f"{x[num][:-1]}%\n"
                     f"{x[num][:-1]}%%\n"
                     f"{x[num][:-1]}^\n"
                     f"{x[num][:-1]}^^\n"
                     f"{x[num][:-1]}&\n"
                     f"{x[num][:-1]}&&\n"
                     f"{x[num][:-1]}*\n"
                     f"{x[num][:-1]}**\n"
                     f"{x[num][:-1]}(\n"
                     f"{x[num][:-1]}((\n"
                     f"{x[num][:-1]})\n"
                     f"{x[num][:-1]}))\n"
                     f"{x[num][:-1]}()\n"
                     f"{x[num][:-1]}(())\n"
                     f"{x[num][:-1]}_\n"
                     f"{x[num][:-1]}__\n"
                     f"{x[num][:-1]}-\n"
                     f"{x[num][:-1]}--\n"
                     f"{x[num][:-1]}+\n"
                     f"{x[num][:-1]}++\n"
                     f"{x[num][:-1]}=\n"
                     f"{x[num][:-1]}==\n"
                     f"{x[num][:-1]}/\n"
                     f"{x[num][:-1]}//\n"
                     f"{x[num][:-1]},\n"
                     f"{x[num][:-1]},,\n"
                     f"{x[num][:-1]}.\n"
                     f"{x[num][:-1]}..\n"
                     f"!{x[num][:-1]}!\n"
                     f"!!{x[num][:-1]}!!\n"
                     f"@{x[num][:-1]}@\n"
                     f"@@{x[num][:-1]}@@\n"
                     f"#{x[num][:-1]}#\n"
                     f"##{x[num][:-1]}##\n"
                     f"${x[num][:-1]}$\n"
                     f"$${x[num][:-1]}$$\n"
                     f"%{x[num][:-1]}%\n"
                     f"%%{x[num][:-1]}%%\n"
                     f"^{x[num][:-1]}^\n"
                     f"^^{x[num][:-1]}^^\n"
                     f"&{x[num][:-1]}&\n"
                     f"&&{x[num][:-1]}&&\n"
                     f"*{x[num][:-1]}*\n"
                     f"**{x[num][:-1]}**\n"
                     f"){x[num][:-1]}(\n"
                     f")){x[num][:-1]}((\n"
                     f"(({x[num][:-1]}))\n"
                     f"_{x[num][:-1]}_\n"
                     f"__{x[num][:-1]}__\n"
                     f"-{x[num][:-1]}-\n"
                     f"+{x[num][:-1]}+\n"
                     f"++{x[num][:-1]}++\n"
                     f"={x[num][:-1]}=\n"
                     f"=={x[num][:-1]}==\n"
                     f".{x[num][:-1]}.\n"
                     f"..{x[num][:-1]}..\n"
                     f",{x[num][:-1]},\n"
                     f",,{x[num][:-1]},,\n")
        openxx.close()
        num -=1

    xq.close()
    return ""
