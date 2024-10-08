from experta import *

from Starter import Starter


class Pastries(Fact):
    pass


class PastriesEngine(KnowledgeEngine):

    @DefFacts()
    def initial(self):
        print("مكونات صنع العجين:")
        print("سكر,الخميرة الفورية, ماء دافئ, طحين, حليب, زيت ذرة")
        yield Pastries(oil=input("هل لديك زيت؟ ( نعم ، لا ) :: "))

    @Rule(Pastries(oil="نعم"))
    def pastries_rule01(self):
        self.declare(Pastries(tomato=input("هل لديك بندورة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
        )
    )
    def pastries_rule02(self):
        self.declare(Pastries(capsicum=input("هل لديك فليفلة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="نعم"),
        )
    )
    def pastries_rule03(self):
        self.declare(Pastries(onion=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="نعم"),
            Pastries(onion="نعم"),
        )
    )
    def pastries_rule04(self):
        print("______________________________")
        print("الوجبة      : فطاير محمرة     ")
        print("يمكنك إضافة : سمسم، حبة البركة")
        print("______________________________")

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="نعم"),
            Pastries(onion="لا"),
        )
    )
    def pastries_rule05(self):
        self.declare(Pastries(oregano=input("هل لديك اوريجانو؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="نعم"),
            Pastries(onion="لا"),
            Pastries(oregano="نعم"),
        )
    )
    def pastries_rule06(self):
        self.declare(Pastries(kashkaval=input("هل لديك قشقوان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="نعم"),
            Pastries(onion="لا"),
            Pastries(oregano="نعم"),
            Pastries(kashkaval="نعم"),
        )
    )
    def pastries_rule07(self):
        print("______________________________")
        print("الوجبة      :       بيتزا     ")
        print("يمكنك إضافة :   زيتون، فطر    ")
        print("______________________________")

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="لا"),
        )
    )
    def pastries_rule08(self):
        self.declare(Pastries(onion=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="لا"),
            Pastries(onion="نعم"),
        )
    )
    def pastries_rule09(self):
        self.declare(Pastries(meat=input("هل لديك لحمة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="لا"),
            Pastries(onion="نعم"),
            Pastries(meat="نعم"),
        )
    )
    def pastries_rule10(self):
        print("______________________________")
        print("الوجبة      :    برك لحمة     ")
        print("______________________________")

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="لا"),
            Pastries(onion="نعم"),
            Pastries(meat="لا"),
        )
    )
    def pastries_rule11(self):
        self.declare(Pastries(Thyme=input("هل لديك زعتر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="نعم"),
            Pastries(capsicum="لا"),
            Pastries(onion="نعم"),
            Pastries(meat="لا"),
            Pastries(Thyme="نعم"),
        )
    )
    def pastries_rule12(self):
        print("______________________________")
        print("الوجبة      :  فطاير زعتر     ")
        print("يمكنك إضافة :   زيتون، فطر    ")
        print("______________________________")

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="لا"),
        )
    )
    def pastries_rule13(self):
        self.declare(Pastries(cheese=input("هل لديك جبنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="لا"),
            Pastries(cheese="نعم"),
        )
    )
    def pastries_rule14(self):
        self.declare(Pastries(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="نعم"),
            Pastries(tomato="لا"),
            Pastries(cheese="نعم"),
            Pastries(egg="نعم"),
        )
    )
    def pastries_rule15(self):
        print("______________________________")
        print("الوجبة      :    برك جبنة     ")
        print("يمكنك إضافة :   بقدونس، عصفر  ")
        print("______________________________")

    @Rule(Pastries(oil="لا"))
    def pastries_rule16(self):
        self.declare(Pastries(fatness=input("هل لديك سمنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="لا"),
            Pastries(fatness="نعم"),
        )
    )
    def pastries_rule17(self):
        self.declare(Pastries(cheese=input("هل لديك جبنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="لا"),
            Pastries(fatness="نعم"),
            Pastries(cheese="نعم"),
        )
    )
    def pastries_rule18(self):
        self.declare(Pastries(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="لا"),
            Pastries(fatness="نعم"),
            Pastries(cheese="نعم"),
            Pastries(egg="نعم"),
        )
    )
    def pastries_rule19(self):
        print("______________________________")
        print("الوجبة      :    فطاير جبنة   ")
        print("يمكنك إضافة :  بقدونس، أريشة  ")
        print("______________________________")

    @Rule(
        AND(
            Pastries(oil="لا"),
            Pastries(fatness="لا"),
        )
    )
    def pastries_rule20(self):
        self.declare(Pastries(shesh=input("هل لديك شيش؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="لا"),
            Pastries(fatness="لا"),
            Pastries(shesh="نعم"),
        )
    )
    def pastries_rule21(self):
        self.declare(Pastries(bharat_shesh=input("هل لديك بهارات شيش؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Pastries(oil="لا"),
            Pastries(fatness="لا"),
            Pastries(shesh="نعم"),
            Pastries(bharat_shesh="نعم"),
        )
    )
    def pastries_rule22(self):
        print("_______________________________")
        print("الوجبة      :    فطاير شيش     ")
        print("يمكنك إضافة :       فطر        ")
        print("_______________________________")

    @Rule(
        OR(
            AND(
                Pastries(oil="لا"), Pastries(fatness="لا"), Pastries(shesh="لا"),
            ),
            AND(
                Pastries(oil="لا"), Pastries(fatness="نعم"), Pastries(shesh="لا"),
            ),
            AND(
                Pastries(oil="لا"), Pastries(fatness="نعم"), Pastries(cheese="لا"),
            ),
            AND(
                Pastries(oil="نعم"), Pastries(tomato="لا"), Pastries(cheese="لا"),
            ),
            AND(
                Pastries(oil="نعم"), Pastries(tomato="لا"),
                Pastries(cheese="نعم"), Pastries(egg="لا"),
            ),
            AND(
                Pastries(oil="لا"), Pastries(fatness="لا"),
                Pastries(shesh="نعم"), Pastries(bharat_shesh="لا"),
            ),
            AND(
                Pastries(oil="لا"), Pastries(fatness="نعم"),
                Pastries(cheese="نعم"), Pastries(egg="لا"),
            ),
            AND(
                Pastries(oil="نعم"), Pastries(tomato="نعم"),
                Pastries(capsicum="لا"), Pastries(onion="نعم"),
                Pastries(meat="لا"), Pastries(Thyme="لا"),
            ),
            AND(
                Pastries(oil="نعم"), Pastries(tomato="نعم"),
                Pastries(capsicum="نعم"), Pastries(onion="لا"),
                Pastries(oregano="لا")
            ),
            AND(
                Pastries(oil="نعم"), Pastries(tomato="نعم"),
                Pastries(capsicum="نعم"), Pastries(onion="لا"),
                Pastries(oregano="نعم"), Pastries(kashkaval="لا"),
            ),
            AND(
                Pastries(oil="نعم"), Pastries(tomato="نعم"),
                Pastries(capsicum="لا"), Pastries(onion="لا"),
            )
        )

    )
    def pastries_rule23(self):
        print("______________________________")
        print("    قم بإعادة طلب المعجنات")
        print("______________________________")
