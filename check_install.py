import pkg_resources

required_packages = [
    ('flake8', '5.0.4'),
    ('flake8-annotations', '2.9.1'),
    ('flake8-quotes', '3.3.1'),
    ('flake8-variables-names', '0.0.5'),
    ('pep8-naming', '0.13.2'),
    ('pytest', '7.1.3'),
    ('iniconfig', '2.3.0')  # Esta es la versión que suele venir con pytest 7.1.3
]

print("Verificando instalación...")
print("-" * 40)

all_ok = True
for package, expected_version in required_packages:
    try:
        installed_version = pkg_resources.get_distribution(package).version
        if installed_version == expected_version:
            print(f"✅ {package:30} {installed_version:10} (OK)")
        else:
            print(f"⚠️  {package:30} {installed_version:10} (esperaba {expected_version})")
            all_ok = False
    except pkg_resources.DistributionNotFound:
        print(f"❌ {package:30} NO INSTALADO")
        all_ok = False

print("-" * 40)
if all_ok:
    print("✅ Todas las librerías están instaladas correctamente")
else:
    print("❌ Hay problemas con algunas librerías")