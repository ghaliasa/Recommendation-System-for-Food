from experta import *

from AnimalFood import AnimalFood


class Sweets(Fact):
    pass


class SweetsEngine(KnowledgeEngine):

    @DefFacts()
    def initial(self):
        yield Sweets(milk=input("هل لديك حليب؟ ( نعم ، لا ) :: "))

    @Rule(Sweets(milk="نعم"))
    def sweets_rule01(self):
        self.declare(Sweets(vanilia=input("هل لديك فانيليا؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
        )
    )
    def sweets_rule02(self):
        self.declare(Sweets(starch=input("هل لديك نشاء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="نعم"),
        )
    )
    def sweets_rule03(self):
        self.declare(Sweets(flower_water=input("هل لديك ماء زهر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
        )
    )
    def sweets_rule04(self):
        self.declare(Sweets(nerg=input("هل لديك ورق نانرج؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
            Sweets(nerg="نعم"),
        )
    )
    def sweets_rule05(self):
        self.declare(Sweets(rise=input("هل لديك رز مسلوق؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
            Sweets(nerg="نعم"), Sweets(rise="نعم"),
        )
    )
    def sweets_rule06(self):
        print("______________________________")
        print("الوجبة      :    رز بحليب     ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
            Sweets(nerg="نعم"), Sweets(rise="لا"),
        )
    )
    def sweets_rule07(self):
        self.declare(Sweets(Wheat=input("هل لديك قمح؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
            Sweets(nerg="نعم"), Sweets(rise="لا"),
            Sweets(Wheat="نعم"),
        )
    )
    def sweets_rule08(self):
        print("______________________________")
        print("الوجبة      :    حبوب     ")
        print("يمكنك إضافة : باقي حبوب البقوليات    ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
            Sweets(nerg="لا"),
        )
    )
    def sweets_rule09(self):
        self.declare(Sweets(crema=input("هل لديك كريمة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"), Sweets(vanilia="نعم"),
            Sweets(starch="نعم"), Sweets(flower_water="نعم"),
            Sweets(nerg="لا"), Sweets(crema="نعم"),
        )
    )
    def sweets_rule10(self):
        print("______________________________")
        print("الوجبة      : محلاية     ")
        print("يمكنك إضافة : مكسرات    ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
        )
    )
    def sweets_rule11(self):
        self.declare(Sweets(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="نعم"),
        )
    )
    def sweets_rule12(self):
        self.declare(Sweets(flour=input("هل لديك طحين؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
        )
    )
    def sweets_rule13(self):
        self.declare(Sweets(oil=input("هل لديك زيت؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
            Sweets(oil="نعم"),

        )
    )
    def sweets_rule14(self):
        self.declare(Sweets(backing_boder=input("هل لديك باكينج باودر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
            Sweets(oil="نعم"),
            Sweets(backing_boder="نعم"),

        )
    )
    def sweets_rule15(self):
        print("______________________________")
        print("الوجبة      :   كيك     ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="لا"),
        )
    )
    def sweets_rule16(self):
        self.declare(Sweets(crema=input("هل لديك كريمة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="لا"),
            Sweets(crema="نعم"),
        )
    )
    def sweets_rule17(self):
        self.declare(Sweets(sugar_apple=input("هل لديك قشطة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="نعم"),
            Sweets(vanilia="نعم"),
            Sweets(starch="لا"),
            Sweets(egg="لا"),
            Sweets(crema="نعم"),
            Sweets(sugar_apple="نعم"),
        )
    )
    def sweets_rule18(self):
        print("______________________________")
        print("الوجبة      : بوظة عربي    ")
        print("يمكنك إضافة : مكسرات , ماء زهر    ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="لا"),

        )
    )
    def sweets_rule19PP(self):
        self.declare(Sweets(vanilia=input("هل لديك فانيليا؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="نعم"),
        )
    )
    def sweets_rule19(self):
        self.declare(Sweets(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="نعم"),
            Sweets(egg="نعم"),
        )
    )
    def sweets_rule20(self):
        self.declare(Sweets(flour=input("هل لديك طحين؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="نعم"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
        )
    )
    def sweets_rule21(self):
        self.declare(Sweets(fatness=input("هل لديك سمنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="نعم"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
            Sweets(fatness="نعم"),
        )
    )
    def sweets_rule22(self):
        self.declare(Sweets(jam=input("هل لديك مربى؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="نعم"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
            Sweets(fatness="نعم"),
            Sweets(jam="نعم"),
        )
    )
    def sweets_rule23(self):
        self.declare(Sweets(backing_boder=input("هل لديك باكينغ باودر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="نعم"),
            Sweets(egg="نعم"),
            Sweets(flour="نعم"),
            Sweets(fatness="نعم"),
            Sweets(jam="نعم"),
            Sweets(backing_boder="نعم"),
        )
    )
    def sweets_rule24(self):
        print("______________________________")
        print("الوجبة      :   حجار القلعة     ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
        )
    )
    def sweets_rule25(self):
        self.declare(Sweets(fatness=input("هل لديك سمنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="نعم"),
        )
    )
    def sweets_rule26(self):
        self.declare(Sweets(semolina=input("هل لديك سميد؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="نعم"),
            Sweets(semolina="نعم"),
        )
    )
    def sweets_rule27(self):
        self.declare(Sweets(yogurt=input("هل لديك لبن؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="نعم"),
            Sweets(semolina="نعم"),
            Sweets(yogurt="نعم"),
        )
    )
    def sweets_rule28(self):
        self.declare(Sweets(katr=input("هل لديك قطر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="نعم"),
            Sweets(semolina="نعم"),
            Sweets(yogurt="نعم"),
            Sweets(katr="نعم"),
        )
    )
    def sweets_rule29(self):
        self.declare(Sweets(water=input("هل لديك ماء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="نعم"),
            Sweets(semolina="نعم"),
            Sweets(yogurt="نعم"),
            Sweets(katr="نعم"),
            Sweets(water="نعم"),
        )
    )
    def sweets_rule30(self):
        print("______________________________")
        print("الوجبة      :   هريسة     ")
        print("______________________________")

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="لا"),
        )
    )
    def sweets_rule31(self):
        self.declare(Sweets(karaweah=input("هل لديك كراويه؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="لا"),
            Sweets(karaweah="نعم"),
        )
    )
    def sweets_rule32(self):
        self.declare(Sweets(water=input("هل لديك ماء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sweets(milk="لا"),
            Sweets(vanilia="لا"),
            Sweets(fatness="لا"),
            Sweets(karaweah="نعم"),
            Sweets(water="نعم"),
        )
    )
    def sweets_rule33(self):
        print("______________________________")
        print("الوجبة      : كراويه   ")
        print("يمكنك إضافة : مكسرات , جوز هند   ")
        print("______________________________")

    @Rule(
        OR(
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="نعم"), Sweets(flower_water="نعم"),
                Sweets(nerg="نعم"), Sweets(rise="لا"),
                Sweets(Wheat="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="نعم"), Sweets(flower_water="نعم"),
                Sweets(nerg="لا"), Sweets(crema="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="نعم"), Sweets(flower_water="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="لا"), Sweets(egg="نعم"),
                Sweets(flour="نعم"), Sweets(oil="نعم"),
                Sweets(backing_boder="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="لا"), Sweets(egg="نعم"),
                Sweets(flour="نعم"), Sweets(oil="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="لا"), Sweets(egg="نعم"),
                Sweets(flour="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="لا"), Sweets(egg="لا"),
                Sweets(crema="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="نعم"),
                Sweets(starch="لا"), Sweets(egg="لا"),
                Sweets(crema="نعم"), Sweets(sugar_apple="لا"),
            ),
            AND(
                Sweets(milk="نعم"), Sweets(vanilia="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="نعم"), Sweets(egg="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="نعم"), Sweets(egg="نعم"),
                Sweets(flour="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="نعم"), Sweets(egg="نعم"),
                Sweets(flour="نعم"), Sweets(fatness="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="نعم"), Sweets(egg="نعم"),
                Sweets(flour="نعم"), Sweets(fatness="نعم"), Sweets(jam="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="نعم"), Sweets(egg="نعم"),
                Sweets(flour="نعم"), Sweets(fatness="نعم"), Sweets(jam="نعم"), Sweets(backing_boder="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="لا"),
                Sweets(fatness="لا"), Sweets(karaweah="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="لا"),
                Sweets(fatness="نعم"), Sweets(semolina="نعم"),
                Sweets(yogurt="نعم"), Sweets(katr="نعم"),
                Sweets(water="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="لا"),
                Sweets(fatness="نعم"), Sweets(semolina="نعم"),
                Sweets(yogurt="نعم"), Sweets(katr="لا"),
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="لا"),
                Sweets(fatness="نعم"), Sweets(semolina="نعم"),
                Sweets(yogurt="لا")
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="لا"),
                Sweets(fatness="نعم"), Sweets(semolina="لا")
            ),
            AND(
                Sweets(milk="لا"), Sweets(vanilia="لا"),
                Sweets(fatness="لا"), Sweets(karaweah="نعم"), Sweets(water="لا"),
            ),
        )
    )
    def sweets_rule34(self):
        print("______________________________")
        print("    قم بإعادة طلب الحلويات")
        print("______________________________")
