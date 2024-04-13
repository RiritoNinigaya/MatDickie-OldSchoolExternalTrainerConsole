from uniref import WinUniRef

unity_oldschool = WinUniRef("Old School.exe")

def Main():
    asm_csharp = unity_oldschool.find_class_in_image("Assembly-CSharp", "Character")
    offset_health = asm_csharp.find_field("health")
    for offset in asm_csharp.guess_instance_address():
        offset_health.set_instance(offset)
        print(offset_health.value)
if __name__ == "__main__":
    Main()