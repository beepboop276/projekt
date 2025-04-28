import json
from openai import OpenAI

# Asenda see oma OpenAI API võtmega
api_key = "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"

# Loome OpenAI kliendi
client = OpenAI(api_key=api_key)

# Funktsioon, mis tekitab treeningkava
def tekitatreeningkava(parameetrid):
    model = "gpt-3.5-turbo"  # Vali sobiv OpenAI mudel
    messages = [
        {
            "role": "user",
            "content": f"Sa saad kasutajalt parameetrid ja väljastad ilusas formaadis treeningkava selle kasutaja jaoks. Parameetrid on: {', '.join(parameetrid)}"
        },
    ]
    temperature = 0.7  # Määra sobiv temperatuur vastuse varieeruvuse jaoks
    max_tokens = 500    # Määra maksimaalne vastuse pikkus
    top_p = 1
    stream = False
    stop = None

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=stream,
            stop=stop,
        )
        vastus = completion.choices[0].message.content
        return vastus
    except Exception as e:
        return f"Viga treeningkava loomisel: {e}"

# Küsime kasutajalt parameetrid
parameetrid_sisend = input("Palun sisesta treeningkava parameetrid (nt eesmärk, treenimissagedus, eelistatud alad): ")
parameetrid = [p.strip() for p in parameetrid_sisend.split(",")]

# Kutsume funktsiooni
treeningkava = tekitatreeningkava(parameetrid)

# Väljastame treeningkava
print("\nGenereeritud treeningkava:\n")
print(treeningkava)

# Salvestame treeningkava json faili
with open('treeningkava.json', 'w', encoding='utf-8') as f:
    json.dump({"parameetrid": parameetrid, "treeningkava": treeningkava}, f, ensure_ascii=False, indent=4)

print("\nTreeningkava on salvestatud faili 'treeningkava.json'.")