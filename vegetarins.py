from experta import *


class Vegetarian(Fact):
    pass


class VegetarianEngine(KnowledgeEngine):

    @DefFacts()
    def initial(self):
        yield Vegetarian(oil=input("هل لديك زيت؟ ( نعم ، لا ) :: "))

    @Rule(Vegetarian(oil="نعم"))
    def vegetarian_rul01(self):
        self.declare(Vegetarian(bulgur=input("هل لديك برغل ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="نعم"),
        )
    )
    def vegetarian_rules02(self):
        self.declare(Vegetarian(zucchini=input("هل لديك كوسا ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="نعم"),
            Vegetarian(zucchini="نعم"),
        )
    )
    def vegetarian_rule03(self):
        print("______________________________")
        print("الوجبة      : برغل بكوسا    ")
        print("يمكنك إضافة : القليل من اللحمة حسب الرغبة ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="نعم"),
            Vegetarian(zucchini="لا"),
        )
    )
    def vegetarian_rule04(self):
        self.declare(Vegetarian(Bean=input("هل لديك فول؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="نعم"),
            Vegetarian(zucchini="لا"),
            Vegetarian(Bean="نعم"),
        )
    )
    def vegetarian_rule05(self):
        print("______________________________")
        print("الوجبة      : برغل بفول    ")
        print("يمكنك إضافة : القليل من اللحمة حسب الرغبة ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="نعم"),
            Vegetarian(zucchini="لا"),
            Vegetarian(Bean="لا"),
        )
    )
    def vegetarian_rule06(self):
        self.declare(Vegetarian(Tomato=input("هل لديك بندورة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="نعم"),
            Vegetarian(zucchini="لا"),
            Vegetarian(Bean="لا"),
            Vegetarian(Tomato="نعم"),

        )
    )
    def vegetarian_rule07(self):
        print("______________________________")
        print("الوجبة      : برغل ببندورة   ")
        print("يمكنك إضافة : القليل من اللحمة حسب الرغبة ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),

        )
    )
    def vegetarian_rule08(self):
        self.declare(Vegetarian(Agine=input("هل لديك عجين ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),

        )
    )
    def vegetarian_rule09(self):
        self.declare(Vegetarian(Adas=input("هل لديك عدس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="نعم"),

        )
    )
    def vegetarian_rule10(self):
        self.declare(Vegetarian(onion=input("هل لديك بصل ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="نعم"),
            Vegetarian(onion="نعم"),

        )
    )
    def vegetarian_rule11(self):
        self.declare(Vegetarian(Tamrhindi=input("هل لديك تمر هندي ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="نعم"),
            Vegetarian(onion="نعم"),
            Vegetarian(Tamrhindi="نعم"),

        )
    )
    def vegetarian_rule12(self):
        self.declare(Vegetarian(D_Roman=input("هل لديك دبس رمان ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="نعم"),
            Vegetarian(onion="نعم"),
            Vegetarian(Tamrhindi="نعم"),
            Vegetarian(D_Roman="نعم"),

        )
    )
    def vegetarian_rule13(self):
        print("______________________________")
        print("الوجبة      :    حراق بأصبعو     ")
        print("الأفضل إضافة :   خبز مقلي وكزبرة *_^  ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="لا"),
        )
    )
    def vegetarian_rule14(self):
        self.declare(Vegetarian(Sabanegh=input("هل لديك سبانخ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="لا"),
            Vegetarian(Sabanegh="نعم"),
        )
    )
    def vegetarian_rule15(self):
        self.declare(Vegetarian(D_Roman=input("هل لديك دبس رمان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="لا"),
            Vegetarian(Sabanegh="نعم"),
            Vegetarian(D_Roman="نعم"),
        )
    )
    def vegetarian_rule16(self):
        self.declare(Vegetarian(Nut=input("هل لديك جوز ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="نعم"),
            Vegetarian(Adas="لا"),
            Vegetarian(Sabanegh="نعم"),
            Vegetarian(D_Roman="نعم"),
            Vegetarian(Nut="نعم"),
        )
    )
    def vegetarian_rule17(self):
        print("______________________________")
        print("الوجبة      :    فطائر سبانخ     ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
        )
    )
    def vegetarian_rule18(self):
        self.declare(Vegetarian(Adas=input("هل لديك عدس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="نعم"),

        )
    )
    def vegetarian_rule19(self):
        self.declare(Vegetarian(onion=input("هل لديك بصل ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="نعم"),
            Vegetarian(onion="نعم"),

        )
    )
    def vegetarian_rule20(self):
        self.declare(Vegetarian(Rice=input("هل لديك رز ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="نعم"),
            Vegetarian(onion="نعم"),
            Vegetarian(Rice="نعم"),

        )
    )
    def vegetarian_rule21(self):
        print("______________________________")
        print("الوجبة      :   مجدرة بالرز     ")
        print("يمكن الاستعاضة عن الرز بالبرغل    ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
        )
    )
    def vegetarian_rule22(self):
        self.declare(Vegetarian(Macaroni=input("هل لديك معكرونة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),

        )
    )
    def vegetarian_rule23(self):
        self.declare(Vegetarian(Tahina=input("هل لديك طحينة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="نعم"),

        )
    )
    def vegetarian_rule24(self):
        self.declare(Vegetarian(Laban=input("هل لديك لبن ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="نعم"),
            Vegetarian(Laban="نعم"),
        )
    )
    def vegetarian_rule25(self):
        print("______________________________")
        print("الوجبة      :   معكرونة باللبن     ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),

        )
    )
    def vegetarian_rule26(self):
        self.declare(Vegetarian(cheese=input("هل لديك جبنة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),
            Vegetarian(cheese="نعم"),

        )
    )
    def vegetarian_rule27(self):
        self.declare(Vegetarian(Bakdounes=input("هل لديك بقدونس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),
            Vegetarian(cheese="نعم"),
            Vegetarian(Bakdounes="نعم"),

        )
    )
    def vegetarian_rule28(self):
        print("______________________________")
        print("الوجبة      :   معكرونة بجبنة    ")
        print("    يمكنك إضافة حبة البركة لتزيين الطبق     ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),
            Vegetarian(cheese="لا"),

        )
    )
    def vegetarian_rule29(self):
        self.declare(Vegetarian(Sous_bashamil=input("هل لديك صوص بشاميل ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),
            Vegetarian(cheese="لا"),
            Vegetarian(Sous_bashamil="نعم"),

        )
    )
    def vegetarian_rule30(self):
        self.declare(Vegetarian(Krema=input("هل لديك كريمة الطبخ ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),
            Vegetarian(cheese="لا"),
            Vegetarian(Sous_bashamil="نعم"),
            Vegetarian(Krema="نعم"),

        )
    )
    def vegetarian_rule31(self):
        self.declare(Vegetarian(Kashkawan=input("هل لديك قشقوان ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="نعم"),
            Vegetarian(Tahina="لا"),
            Vegetarian(cheese="لا"),
            Vegetarian(Sous_bashamil="نعم"),
            Vegetarian(Krema="نعم"),
            Vegetarian(Kashkawan="نعم"),
        )
    )
    def vegetarian_rule28PP(self):
        print("______________________________")
        print("الوجبة      :   معكرونة بشاميل    ")
        print("    يمكنك إضافة القليل من قطع الدجاج في حال الرغبة     ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="لا"),
        )
    )
    def vegetarian_rule32(self):
        self.declare(Vegetarian(Bean=input("هل لديك فول ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="لا"),
            Vegetarian(Bean="نعم"),

        )
    )
    def vegetarian_rule33(self):
        self.declare(Vegetarian(Kizbara=input("هل لديك كزبرة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="لا"),
            Vegetarian(Bean="نعم"),
            Vegetarian(Kizbara="نعم"),
        )
    )
    def vegetarian_rule34(self):
        print("______________________________")
        print("الوجبة     فول مقلى    ")
        print("    يمكنك إضافة التوم في حال الرغبة    ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="لا"),
            Vegetarian(Bean="لا"),

        )
    )
    def vegetarian_rule35(self):
        self.declare(Vegetarian(Fasolia=input("هل لديك فاصولياء ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="لا"),
            Vegetarian(Bean="لا"),
            Vegetarian(Fasolia="نعم"),

        )
    )
    def vegetarian_rule36(self):
        self.declare(Vegetarian(Tomato=input("هل لديك بندورة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="نعم"),
            Vegetarian(bulgur="لا"),
            Vegetarian(Agine="لا"),
            Vegetarian(Adas="لا"),
            Vegetarian(Macaroni="لا"),
            Vegetarian(Bean="لا"),
            Vegetarian(Fasolia="نعم"),
            Vegetarian(Tomato="نعم"),
        )
    )
    def vegetarian_rule37(self):
        print("______________________________")
        print("الوجبة      :   فاصولياء بالزيت    ")
        print("    يمكنك إضافة الثوم والبصل في حال الرغبة     ")
        print("صحة وهنا  *_^  ")
        print("______________________________")

    @Rule(Vegetarian(oil="لا"))
    def vegetarian_rule38(self):
        self.declare(Vegetarian(Kosa=input("هل لديك كوسا ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="نعم"),

        )
    )
    def vegetarian_rule39(self):
        self.declare(Vegetarian(Betngan=input("هل لديك باذنجان ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
        )
    )
    def vegetarian_rule39PP(self):
        self.declare(Vegetarian(Betngan=input("هل لديك باذنجان ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="نعم"),
            Vegetarian(Betngan="نعم"),

        )
    )
    def vegetarian_rule40(self):
        self.declare(Vegetarian(mint=input("هل لديك نعنع ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="نعم"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(mint="نعم"),

        )
    )
    def vegetarian_rule41(self):
        self.declare(Vegetarian(Tomato=input("هل لديك بندورة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="نعم"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(mint="نعم"),
            Vegetarian(Tomato="نعم"),

        )
    )
    def vegetarian_rule42(self):
        self.declare(Vegetarian(pepper=input("هل لديك فليفلة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="نعم"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(mint="نعم"),
            Vegetarian(Tomato="نعم"),
            Vegetarian(pepper="نعم"),
        )
    )
    def vegetarian_rule43PP(self):
        print("______________________________")
        print("الوجبة      :   طباخ روحو    ")
        print("      يمكنك إضافة الثوم أو البصل أو اللحمة      ")
        print("    وينصح بوضع القليل من الزيت إن وجد لزكاوة الطعم    ")
        print("بالهناء والشفاء  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="نعم"),

        )
    )
    def vegetarian_rule44(self):
        self.declare(Vegetarian(D_Roman=input("هل لديك دبس رمان ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(D_Roman="نعم"),

        )
    )
    def vegetarian_rule45(self):
        self.declare(Vegetarian(bread=input("هل لديك خبز ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(D_Roman="نعم"),
            Vegetarian(bread="نعم"),

        )
    )
    def vegetarian_rule46(self):
        self.declare(Vegetarian(Laban=input("هل لديك لبن ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(D_Roman="نعم"),
            Vegetarian(bread="نعم"),
            Vegetarian(Laban="نعم"),

        )
    )
    def vegetarian_rule47(self):
        self.declare(Vegetarian(Tahina=input("هل لديك طحينة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="نعم"),
            Vegetarian(D_Roman="نعم"),
            Vegetarian(bread="نعم"),
            Vegetarian(Laban="نعم"),
            Vegetarian(Tahina="نعم"),
        )
    )
    def vegetarian_rule48(self):
        print("______________________________")
        print("الوجبة      :   فتة مكدوس    ")
        print("      يمكنك إضافة اللحمة في حال الرغبة      ")
        print("    قد  تحتاج للقليل من الزيت للتمكن من قلي الخبز  ")
        print("بالهناء والشفاء  *_^  ")
        print("______________________________")

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
        )
    )
    def vegetarian_rule49(self):
        self.declare(Vegetarian(grape_leaves=input("هل لديك ورق عنب ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
            Vegetarian(grape_leaves="نعم"),

        )
    )
    def vegetarian_rule50(self):
        self.declare(Vegetarian(D_Roman_or_Lemon=input("هل لديك دبس رمان أو ليمون ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
            Vegetarian(grape_leaves="نعم"),
            Vegetarian(D_Roman_or_Lemon="نعم"),
        )
    )
    def vegetarian_rule51(self):
        self.declare(Vegetarian(rice_or_bulgur=input("هل لديك رز أو برغل ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
            Vegetarian(grape_leaves="نعم"),
            Vegetarian(D_Roman_or_Lemon="نعم"),
            Vegetarian(rice_or_bulgur="نعم"),
        )
    )
    def vegetarian_rule52(self):
        self.declare(Vegetarian(Bakdones=input("هل لديك بقدونس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
            Vegetarian(grape_leaves="نعم"),
            Vegetarian(D_Roman_or_Lemon="نعم"),
            Vegetarian(rice_or_bulgur="نعم"),
            Vegetarian(Bakdones="نعم"),
        )
    )
    def vegetarian_rule53(self):
        self.declare(Vegetarian(mint=input("هل لديك نعنع ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
            Vegetarian(grape_leaves="نعم"),
            Vegetarian(D_Roman_or_Lemon="نعم"),
            Vegetarian(rice_or_bulgur="نعم"),
            Vegetarian(Bakdones="نعم"),
            Vegetarian(mint="نعم"),

        )
    )
    def vegetarian_rule52PPP(self):
        self.declare(Vegetarian(Tomato=input("هل لديك بندورة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Vegetarian(oil="لا"),
            Vegetarian(Kosa="لا"),
            Vegetarian(Betngan="لا"),
            Vegetarian(grape_leaves="نعم"),
            Vegetarian(D_Roman_or_Lemon="نعم"),
            Vegetarian(rice_or_bulgur="نعم"),
            Vegetarian(Bakdones="نعم"),
            Vegetarian(mint="نعم"),
            Vegetarian(Tomato="نعم"),
        )
    )
    def vegetarian_rule54AA(self):
        print("______________________________")
        print("الوجبة      :  يالانجي    ")
        print("      يمكنك إضافة البصل والقلي من البن لإضفاء نكهة مميزة     ")
        print("    قد تحتاج للقليل من الزيت داخل حشوة اليالانجي    ")
        print("بالهناء والشفاء  *_^  ")
        print("______________________________")

    @Rule(
        OR(
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="نعم"),
                Vegetarian(Adas="نعم"),
                Vegetarian(onion="نعم"),
                Vegetarian(Tamrhindi="نعم"),
                Vegetarian(D_Roman="لا"),
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="نعم"),
                Vegetarian(Adas="نعم"),
                Vegetarian(onion="نعم"),
                Vegetarian(Tamrhindi="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="نعم"),
                Vegetarian(Adas="نعم"),
                Vegetarian(onion="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="نعم"),
                Vegetarian(Adas="لا"),
                Vegetarian(Sabanegh="نعم"),
                Vegetarian(D_Roman="نعم"),
                Vegetarian(Nut="لا"),
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="نعم"),
                Vegetarian(Adas="لا"),
                Vegetarian(Sabanegh="نعم"),
                Vegetarian(D_Roman="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="نعم"),
                Vegetarian(Adas="لا"),
                Vegetarian(Sabanegh="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="نعم"),
                Vegetarian(zucchini="لا"),
                Vegetarian(Bean="لا"),
                Vegetarian(Tomato="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="نعم"),
                Vegetarian(onion="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="نعم"),
                Vegetarian(onion="نعم"),
                Vegetarian(Rice="لا"),
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="لا"),
                Vegetarian(Macaroni="نعم"),
                Vegetarian(Tahina="نعم"),
                Vegetarian(Laban="لا"),
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="لا"),
                Vegetarian(Macaroni="نعم"),
                Vegetarian(Tahina="لا")
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="لا"),
                Vegetarian(Macaroni="لا"),
                Vegetarian(Bean="نعم"),
                Vegetarian(Kizbara="لا"),
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="لا"),
                Vegetarian(Macaroni="لا"),
                Vegetarian(Bean="لا"),
                Vegetarian(Fasolia="نعم"),
                Vegetarian(Tomato="لا"),
            ),
            AND(
                Vegetarian(oil="نعم"),
                Vegetarian(bulgur="لا"),
                Vegetarian(Agine="لا"),
                Vegetarian(Adas="لا"),
                Vegetarian(Macaroni="لا"),
                Vegetarian(Bean="لا"),
                Vegetarian(Fasolia="لا")
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="نعم"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(mint="نعم"),
                Vegetarian(Tomato="نعم"),
                Vegetarian(pepper="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="نعم"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(mint="نعم"),
                Vegetarian(Tomato="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="نعم"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(mint="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="نعم"),
                Vegetarian(Betngan="لا")
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(D_Roman="نعم"),
                Vegetarian(bread="نعم"),
                Vegetarian(Laban="نعم"),
                Vegetarian(Tahina="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(D_Roman="نعم"),
                Vegetarian(bread="نعم"),
                Vegetarian(Laban="لا")
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(D_Roman="نعم"),
                Vegetarian(bread="لا")
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="نعم"),
                Vegetarian(D_Roman="لا")
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="نعم"),
                Vegetarian(D_Roman_or_Lemon="نعم"),
                Vegetarian(rice_or_bulgur="نعم"),
                Vegetarian(Bakdones="نعم"),
                Vegetarian(mint="نعم"),
                Vegetarian(Tomato="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="نعم"),
                Vegetarian(D_Roman_or_Lemon="نعم"),
                Vegetarian(rice_or_bulgur="نعم"),
                Vegetarian(Bakdones="نعم"),
                Vegetarian(mint="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="نعم"),
                Vegetarian(D_Roman_or_Lemon="نعم"),
                Vegetarian(rice_or_bulgur="نعم"),
                Vegetarian(Bakdones="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="نعم"),
                Vegetarian(D_Roman_or_Lemon="نعم"),
                Vegetarian(rice_or_bulgur="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="نعم"),
                Vegetarian(D_Roman_or_Lemon="لا"),
            ),
            AND(
                Vegetarian(oil="لا"),
                Vegetarian(Kosa="لا"),
                Vegetarian(Betngan="لا"),
                Vegetarian(grape_leaves="لا"),
            ),

        )
    )
    def vegetarian_rule90(self):
        print("______________________________")
        print("    قم بإعادة طلب الطعام النباتي")
        print("______________________________")
