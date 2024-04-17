from classes.Historia import Historia

title = '¡Vamos a acampar!'
text = '''Este fin de semana voy a acampar con *. Empaqué mi linterna, saco
de dormir, y *. Estoy tan * para * en una tienda de campaña. Estoy * que vamos
a ver un(a) *, que son peligrosos. Vamos a caminar, pescar, y *. He oido que
el lago * es genial para *. Entonces vamos a caminar * por del bosque para * *.
Si veo un(a) * * mientras estoy caminando, ¡lo llevaré a casa como mascota! Por
la noches vamos a contar * * historias y asar * alrededor de la fogata!!'''
type_words = [
        'nombre de la persona',
        'sustantivo',
        'adjetivo (sensacion)',
        'verbo',
        'adjetivo (sensacion)',
        'animal',
        'verbo',
        'color',
        'verbo',
        'adverbio',
        'número',
        'medida de tiempo',
        'animal',
        'color',
        'número',
        'palabra tonta',
        'sustantivo plural'
        ]

h = Historia(title, text, type_words)
h.ask()
h.complete_text()