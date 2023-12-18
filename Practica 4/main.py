from Legion import Legion

print("Creando ejército...")
legion_romana = Legion()
print("Ejército creado")
print("Composición actual: ")
print("- 0 unidades de combate")
print("- 0 oficiales")
print("  (número total de componentes: 0)")
print("Poblando ejército...             ")
legion_romana.poblar()
print("Ejército poblado")
print("Composición actual: ")
print(f"- {legion_romana.obtener_soldados()} unidades de combate")
print(f"- {legion_romana.obtener_oficiales()} oficiales")
print(f"  (número total de componentes: "
      f"{legion_romana.obtener_soldados() + legion_romana.obtener_oficiales()})")
