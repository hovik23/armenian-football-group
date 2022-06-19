# Armenian Football Group Image Creating
## Ներածություն
Այս պրոյեկտը արված ա [Armenian Football Group](https://t.me/armfootballgroup)-ի համար։ Սա իրականացված ա Telegram-ում բոտի միջոցով։ Այս ծրագրի շնորհիվ կարելի ա ստանալ Հայկական Պրեմյեր Լիգայի թե ուրից ցանկացած առաջնության խաղի պաստառը ավելի հարմար ինֆորմացիայի ընկալման համար։
Այս պրոյեկտը պարունակում ա միայն պաստառներ ստեղծելու կոդը, քանի որ հենց այդ ա ծրագրի հիմքը և անենակարևոր մասը։

## Նախադրյալները
* **[Python 3](https://www.python.org/downloads/)**
* **[Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)**
* **[SQLite](https://docs.python.org/3/library/sqlite3.html)**
* **[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)**

Արթյունքը ներկայացված ա **[armenian-football-group.ipynb](armenian-football-group.ipynb)** ֆայլում Jupyrer Notebook-ի միջոցով։ Հիմնական կոդը գրած ա image.py ֆայլում։ Այդ երկու ֆայլը մի փոքր տարբերվում են, քանի որ մի քանի փոփոխություններ էին անհրաժեշտ դեմոնստրացիայի համար։

## Տվյալների բազա
Տվյալների բազաի համար ընտրված ա SQLite, քանի որ ծրագիրը ենթադրում ա մերքին օգտագործում և որևէ իրավունքների խնդիր չպիտի առաջանա։

Հիմնական բազայի քնթւնը afg.db ա, մեջ կան մի քանի աղուսյակներ։ Առաջին հերթին, teams աղուսյակը պարունակում ա ակումբների անունը 3 լեզվով (Հայերեն, Անգլերեն և Ռուսերեն) և իրանց id-ն որի շնորհիվ հետո եզակիորեն կկապվեն նկարի հետ։ Այսինքն, ակումբի նկարի անունը լինելու ա հետևյալ ֆորմատով՝ `«id».png `

##### teams
| team_id  | name_en | name_ru | name_hy |
| --- | --- | --- |
| 1 | Alashkert | Алашкерт | Ալաշկերտ |
| 2 | Ararat Armenia | Арарат Армения | Արարատ Արմենիա |
| 3 | Ararat | Арарат | Արարատ |
| ... | ... | ... | ... |

##### competitions
| id  | name_en | name_ru | name_hy |
| --- | --- | --- |
| 1 | VBET APL | VBET АПЛ | VBET ՀՊԼ |
| ... | ... | ... | ... |

##### users
| id  | name | nickname | lang |
| --- | --- | --- |
| 86163709 | Hovhannes | hovhannes23 | hy |
| ... | ... | ... | ... |

## Աշխատանքի արթյունքները
![Figure 1](https://github.com/hovik23/armenian-football-group/blob/master/data/results/1.png "Figure 1")
![Figure 2](https://github.com/hovik23/armenian-football-group/blob/master/data/results/2.png "Figure 2")