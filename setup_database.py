from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Base, Item

engine = create_engine('postgresql:///plants.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name="Plantas Terrestres")

session.add(category1)
session.commit()

Item1 = Item(name="Musgos",
             description="""Os musgos são representantes do grupo das briófitas
             e como tal não apresentam vasos lignificados condutores de água e
             sais minerais. """,
             category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="Arbustos",
             description="""Arbusto ou moita é todo o vegetal do grupo das
             angiospermas dicotiledôneas lenhosas, que se ramifica desde junto
             ao solo e tem menor porte em relação às árvores.""",
             category=category1)

session.add(Item2)
session.commit()


category2 = Category(name="Plantas Aquaticas")

session.add(category2)
session.commit()

Item3 = Item(name="Vitoria-Regia",
             description="""A vitória-régia ou victória-régia
             (Victoria amazonica) é uma planta aquática da família das
             Nymphaeaceae, típica da região amazônica.""",
             category=category2)

session.add(Item3)
session.commit()

Item4 = Item(name="Lotus",
             description="""Nelumbo nucifera é uma planta aquática da gênero
             Nelumbo, conhecida popularmente como lótus, flor-de-lótus,
             loto-índico e lótus-índico.""",
             category=category2)

session.add(Item4)
session.commit()


category3 = Category(name="Plantas Aereas")

session.add(category3)
session.commit()

Item5 = Item(name="Filodendro",
             description="""São, em geral, plantas semitrepadeiras, de caule
             frágil, com raízes aéreas pouco resistentes. Possui grandes folhas
             labeladas, e suas flores são minúsculas, agrupadas em forma de
             espiga sob uma capa que se abre quando aptas à fecundação.""",
             category=category3)

session.add(Item5)
session.commit()

Item6 = Item(name="Costela de Adão",
             description="""A costela-de-adão é uma planta da família das
             aráceas. Possui folhas grandes, cordiformes, penatífidas e
             perfuradas, com longos pecíolos, flores aromáticas, em espádice
             comestível, branco-creme, com espata verde, e bagas
             amarelo-claras.""",
             category=category3)

session.add(Item6)
session.commit()


category4 = Category(name="Plantas de Jardim")

session.add(category4)
session.commit()

Item7 = Item(name="Bromelia:",
             description="""É uma flor decorativa que deve ser exposta ao sol
             de forma indireta. É preciso regá-la duas vezes por semana e
             evitar o acúmulo de água na planta.""",
             category=category4)

session.add(Item7)
session.commit()

Item8 = Item(name="Violeta",
             description="""A violeta pode adquirir muitas cores e com seu
             preço acessível é possível decorar muito bem a casa. Deve ser
             regada pelo menos duas vezes por semana e exposta somente a
             luz indireta.""",
             category=category4)

session.add(Item8)
session.commit()


category5 = Category(name="Plantas Ornamentais")

session.add(category5)
session.commit()

Item9 = Item(name="Pau d'água:",
             description="""Planta muito utilizada para decorar escritórios
             porque aguenta a intensidade do ar-condicionado.""",
             category=category5)

session.add(Item9)
session.commit()

Item10 = Item(name="Rosa de Pedra",
              description="""O formato da planta lembra uma rosa e ela é ótima
              para armazenar água. Não deve ser muito exposta ao sol e precisa
              ser regada uma vez por semana.""",
              category=category5)

session.add(Item10)
session.commit()


category6 = Category(name="Plantas Carnívoras")

session.add(category6)
session.commit()

Item11 = Item(name="Dionaea",
              description="""A dioneia é uma planta carnívora que pega e digere
              presa animal.""",
              category=category6)

session.add(Item11)
session.commit()

Item12 = Item(name="Drosera",
              description="""Drosera L. é um género botânico pertencente à
              família Droseraceae.""",
              category=category6)

session.add(Item12)
session.commit()


category7 = Category(name="Plantas Medicinais e Ervas")

session.add(category7)
session.commit()

Item13 = Item(name="Doril",
              description="""doril é o nome de uma flor, que é eficaz contra
              dor de cabeça. Basta tomar um chá de folhas de Doril, mas para
              que ele realmente tenha efeito, é preciso cuidar e deixar a
              planta em ambientes com muita claridade, e regá-la todos os
              dias.""",
              category=category7)

session.add(Item13)
session.commit()

Item14 = Item(name="Romã",
              description="""o chá com os frutos de Romã ameniza a dor de
              garganta, mas é preciso regá-la de dois em dois dias e
              fertilizá-la uma vez por mês.""",
              category=category7)

session.add(Item14)
session.commit()


category8 = Category(name="Plantas Tóxicas ou Venenosas")

session.add(category8)
session.commit()

Item15 = Item(name="Aroeira:",
              description="""Aroeira ou arrueira é o nome popular de várias
              espécies de árvores da família Anacardiaceae.""",
              category=category8)

session.add(Item15)
session.commit()

Item16 = Item(name="Artemísia",
              description="""A Artemísia é uma erva muito conhecida desde
              tempos super antigos por suas propriedades medicinais.""",
              category=category8)

session.add(Item16)
session.commit()

print("items added!")
