from experta import *


class Starter(Fact):
    pass


class StarterEngine(KnowledgeEngine):

    @DefFacts()
    def initial(self):
        yield Starter(bandora=input("هل لديك بندورة؟ ( نعم ، لا ) :: "))

    @Rule(Starter(bandora="نعم"))
    def starter_rule01(self):
        self.declare(Starter(bakdons=input("هل لديك بقدونس؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
        )
    )
    def starter_rule02(self):
        self.declare(Starter(lemon=input("هل لديك ليمون؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
        )
    )
    def starter_rule03(self):
        self.declare(Starter(onin=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
        )
    )
    def starter_rule04(self):
        self.declare(Starter(zit=input("هل لديك زيت؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
        )
    )
    def starter_rule05(self):
        self.declare(Starter(anjinar=input("هل لديك انغينار؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="نعم"),
        )
    )
    def starter_rule06(self):
        print("______________________________")
        print("الوجبة      : سلطة انغينار    ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
        )
    )
    def starter_rule07(self):
        self.declare(Starter(thom=input("هل لديك ثوم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="نعم"),
        )
    )
    def starter_rule08(self):
        self.declare(Starter(homs=input("هل لديك حمص؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="نعم"),
            Starter(homs="نعم"),
        )
    )
    def starter_rule09(self):
        print("______________________________")
        print("الوجبة      :    حمص متبل   ")
        print("يمكنك إضافة :    دبس رمان   ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="نعم"),
            Starter(homs="لا"),
        )
    )
    def starter_rule10(self):
        self.declare(Starter(fool=input("هل لديك فول؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="نعم"),
            Starter(homs="لا"),
            Starter(fool="نعم"),
        )
    )
    def starter_rule11(self):
        print("______________________________")
        print("الوجبة      :     فول مدمس    ")
        print("يمكنك إضافة :     دبس رمان    ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="لا"),
        )
    )
    def starter_rule12(self):
        self.declare(Starter(brghl=input("هل لديك برغل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="لا"),
            Starter(brghl="نعم"),
        )
    )
    def starter_rule13(self):
        self.declare(Starter(Nana=input("هل لديك نعنع؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="نعم"),
            Starter(lemon="نعم"),
            Starter(onin="نعم"),
            Starter(zit="نعم"),
            Starter(anjinar="لا"),
            Starter(thom="لا"),
            Starter(brghl="نعم"),
            Starter(Nana="نعم"),
        )
    )
    def starter_rule14(self):
        print("______________________________")
        print("الوجبة      :      تبولة      ")
        print("يمكنك إضافة :     خيار وخس    ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
        )
    )
    def starter_rule15(self):
        self.declare(Starter(Nana=input("هل لديك نعنع؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
        )
    )
    def starter_rule16(self):
        self.declare(Starter(onin=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
        )
    )
    def starter_rule17(self):
        self.declare(Starter(jrjer=input("هل لديك جرجير؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="نعم"),
        )
    )
    def starter_rule18(self):
        self.declare(Starter(lemon=input("هل لديك ليمون؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="نعم"),
            Starter(lemon="نعم"),
        )
    )
    def starter_rule19(self):
        self.declare(Starter(zit=input("هل لديك زيت؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="نعم"),
            Starter(lemon="نعم"),
            Starter(zit="نعم"),
        )
    )
    def starter_rule20(self):
        print("______________________________")
        print("الوجبة      :    سلطة جرجير   ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="لا"),
        )
    )
    def starter_rule21(self):
        self.declare(Starter(khs=input("هل لديك خس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="لا"),
            Starter(khs="نعم"),
        )
    )
    def starter_rule22(self):
        self.declare(Starter(KhiarAndLemonAndZit=input("هل لديك خيار وليمون وزيت ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="لا"),
            Starter(khs="نعم"),
            Starter(KhiarAndLemonAndZit="نعم"),
        )
    )
    def starter_rule23(self):
        print("______________________________")
        print("الوجبة      :      سلطة       ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="لا"),
            Starter(khs="لا"),
        )
    )
    def starter_rule24(self):
        self.declare(Starter(KhbzMkli=input("هل لديك خبز مقلي  ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="لا"),
            Starter(khs="لا"),
            Starter(KhbzMkli="نعم"),
        )
    )
    def starter_rule25(self):
        self.declare(Starter(KhiarAndLemonAndZitAndBkla=input("هل لديك خيار وليمون وزيت وبقلة  ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="نعم"),
            Starter(bakdons="لا"),
            Starter(Nana="نعم"),
            Starter(onin="نعم"),
            Starter(jrjer="لا"),
            Starter(khs="لا"),
            Starter(KhbzMkli="نعم"),
            Starter(KhiarAndLemonAndZitAndBkla="نعم"),
        )
    )
    def starter_rule26(self):
        print("______________________________")
        print("الوجبة      :      فتووش      ")
        print("يمكنك إضافة :       ثوم       ")
        print("______________________________")

    @Rule(Starter(bandora="لا"))
    def starter_rule27(self):
        self.declare(Starter(bitnjan=input("هل لديك بيتنجان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
        )
    )
    def starter_rule28(self):
        self.declare(Starter(laban=input("هل لديك لبن؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="نعم"),
        )
    )
    def starter_rule29(self):
        self.declare(Starter(thom=input("هل لديك ثوم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="نعم"),
            Starter(thom="نعم"),
        )
    )
    def starter_rule30(self):
        self.declare(Starter(thina=input("هل لديك طحينة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="نعم"),
            Starter(thom="نعم"),
            Starter(thina="نعم"),
        )
    )
    def starter_rule31(self):
        self.declare(Starter(zit=input("هل لديك زيت؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="نعم"),
            Starter(thom="نعم"),
            Starter(thina="نعم"),
            Starter(zit="نعم"),
        )
    )
    def starter_rule32(self):
        print("______________________________")
        print("الوجبة      :      متبل      ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="لا"),
        )
    )
    def starter_rule33(self):
        self.declare(Starter(dbsRman=input("هل لديك دبس رمان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="لا"),
            Starter(dbsRman="نعم"),
        )
    )
    def starter_rule34(self):
        self.declare(Starter(zit=input("هل لديك زيت؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="نعم"),
            Starter(laban="لا"),
            Starter(dbsRman="نعم"),
            Starter(zit="نعم"),
        )
    )
    def starter_rule35(self):
        print("______________________________")
        print("الوجبة      :     بابا غنوج       ")
        print("يمكنك إضافة :     بقدونس وجوز     ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
        )
    )
    def starter_rule36(self):
        self.declare(Starter(laban=input("هل لديك لبن؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="نعم"),
        )
    )
    def starter_rule37(self):
        self.declare(Starter(khiarAndNanaAndWater=input("هل لديك خيار ونعنع وماء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="نعم"),
            Starter(khiarAndNanaAndWater="نعم"),
        )
    )
    def starter_rule38(self):
        print("______________________________")
        print("الوجبة    :   سلطة لبن بخيار  ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
        )
    )
    def starter_rule39(self):
        self.declare(Starter(hmos=input("هل لديك حمص؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="نعم"),
        )
    )
    def starter_rule40(self):
        self.declare(Starter(badwaAndSmnaAndKhbz=input("هل لديك بدوة وسمنة وخبز؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="نعم"),
            Starter(badwaAndSmnaAndKhbz="نعم"),
        )
    )
    def starter_rule41(self):
        print("______________________________")
        print("الوجبة      :    تسقية بسمنة     ")
        print("يمكنك إضافة :     ليمون وجوز     ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
        )
    )
    def starter_rule42(self):
        self.declare(Starter(sh3iria=input("هل لديك شعيرية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="نعم"),
        )
    )
    def starter_rule43(self):
        self.declare(Starter(meatAndRbAlbandoraAndZit=input("هل لديك لحمة ورب البندورة وزيت؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="نعم"),
            Starter(meatAndRbAlbandoraAndZit="نعم"),
        )
    )
    def starter_rule44(self):
        print("______________________________")
        print("الوجبة     :   شوربة شعيرية   ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
        )
    )
    def starter_rule45(self):
        self.declare(Starter(meat=input("هل لديك لحمة ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="نعم"),
        )
    )
    def starter_rule46(self):
        self.declare(Starter(aadaas=input("هل لديك عدس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="نعم"),
            Starter(aadaas="نعم"),
        )
    )
    def starter_rule47(self):
        self.declare(Starter(osfor=input("هل لديك عصفر ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="نعم"),
            Starter(aadaas="نعم"),
            Starter(osfor="نعم"),
        )
    )
    def starter_rule48(self):
        print("______________________________")
        print("الوجبة      :    شوربة عدس       ")
        print("يمكنك إضافة :  ليمون ورز أو برغل ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
        )
    )
    def starter_rule49(self):
        self.declare(Starter(aadaas=input("هل لديك عدس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="نعم"),
        )
    )
    def starter_rule50(self):
        self.declare(
            Starter(oninAndNanaAndZitAndKhbzAndWater=input("هل لديك بصل ونعنع وخبز وزيت وماء ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="نعم"),
            Starter(oninAndNanaAndZitAndKhbzAndWater="نعم"),
        )
    )
    def starter_rule51(self):
        print("______________________________")
        print("الوجبة      :    كشكة       ")
        print("يمكنك إضافة :    ثوم        ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
        )
    )
    def starter_rule52(self):
        self.declare(Starter(batata=input("هل لديك بطاطا ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="نعم"),
        )
    )
    def starter_rule53(self):
        self.declare(Starter(zit=input("هل لديك زيت ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="نعم"),
            Starter(zit="نعم"),
        )
    )
    def starter_rule54(self):
        self.declare(Starter(kashkawan=input("هل لديك قشقوان ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="نعم"),
            Starter(zit="نعم"),
            Starter(kashkawan="نعم"),
        )
    )
    def starter_rule55(self):
        print("______________________________")
        print("الوجبة      :    بطاطا مقلية  ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="نعم"),
            Starter(zit="نعم"),
            Starter(kashkawan="لا"),
        )
    )
    def starter_rule56(self):
        self.declare(Starter(baidAndTahinAndBakdons=input("هل لديك بيض وطحين وبقدونس ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="نعم"),
            Starter(zit="نعم"),
            Starter(kashkawan="لا"),
            Starter(baidAndTahinAndBakdons="نعم"),
        )
    )
    def starter_rule57(self):
        print("______________________________")
        print("الوجبة      :      عجة        ")
        print("______________________________")

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="لا"),
        )
    )
    def starter_rule58(self):
        self.declare(Starter(jaj=input("هل لديك جاج ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="لا"),
            Starter(jaj="نعم"),
        )
    )
    def starter_rule59(self):
        self.declare(
            Starter(hbashatAlSizar=input("هل لديك خس وخبز توست وميونيز وخل واوريجانو وزيت ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Starter(bandora="لا"),
            Starter(bitnjan="لا"),
            Starter(laban="لا"),
            Starter(hmos="لا"),
            Starter(sh3iria="لا"),
            Starter(meat="لا"),
            Starter(aadaas="لا"),
            Starter(batata="لا"),
            Starter(jaj="نعم"),
            Starter(hbashatAlSizar="نعم"),
        )
    )
    def starter_rule60(self):
        print("______________________________")
        print("الوجبة      :    سلطة سيزر    ")
        print("______________________________")

    @Rule(
        OR(
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="نعم"),
                Starter(lemon="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="نعم"),
                Starter(lemon="نعم"),
                Starter(onin="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="نعم"),
                Starter(lemon="نعم"),
                Starter(onin="نعم"),
                Starter(zit="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="نعم"),
                Starter(lemon="نعم"),
                Starter(onin="نعم"),
                Starter(zit="نعم"),
                Starter(anjinar="لا"),
                Starter(thom="نعم"),
                Starter(homs="لا"),
                Starter(fool="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="نعم"),
                Starter(lemon="نعم"),
                Starter(onin="نعم"),
                Starter(zit="نعم"),
                Starter(anjinar="لا"),
                Starter(thom="لا"),
                Starter(brghl="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="نعم"),
                Starter(lemon="نعم"),
                Starter(onin="نعم"),
                Starter(zit="نعم"),
                Starter(anjinar="لا"),
                Starter(thom="لا"),
                Starter(brghl="نعم"),
                Starter(Nana="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="نعم"),
                Starter(onin="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="نعم"),
                Starter(onin="نعم"),
                Starter(jrjer="نعم"),
                Starter(lemon="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="نعم"),
                Starter(onin="نعم"),
                Starter(jrjer="نعم"),
                Starter(lemon="نعم"),
                Starter(zit="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="نعم"),
                Starter(onin="نعم"),
                Starter(jrjer="لا"),
                Starter(khs="نعم"),
                Starter(KhiarAndLemonAndZit="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="نعم"),
                Starter(onin="نعم"),
                Starter(jrjer="لا"),
                Starter(khs="لا"),
                Starter(KhbzMkli="لا"),
            ),
            AND(
                Starter(bandora="نعم"),
                Starter(bakdons="لا"),
                Starter(Nana="نعم"),
                Starter(onin="نعم"),
                Starter(jrjer="لا"),
                Starter(khs="لا"),
                Starter(KhbzMkli="نعم"),
                Starter(KhiarAndLemonAndZitAndBkla="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="نعم"),
                Starter(laban="نعم"),
                Starter(thom="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="نعم"),
                Starter(laban="نعم"),
                Starter(thom="نعم"),
                Starter(thina="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="نعم"),
                Starter(laban="نعم"),
                Starter(thom="نعم"),
                Starter(thina="نعم"),
                Starter(zit="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="نعم"),
                Starter(laban="لا"),
                Starter(dbsRman="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="نعم"),
                Starter(laban="لا"),
                Starter(dbsRman="نعم"),
                Starter(zit="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="نعم"),
                Starter(khiarAndNanaAndWater="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="نعم"),
                Starter(badwaAndSmnaAndKhbz="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="نعم"),
                Starter(meatAndRbAlbandoraAndZit="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="لا"),
                Starter(meat="نعم"),
                Starter(aadaas="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="لا"),
                Starter(meat="نعم"),
                Starter(aadaas="نعم"),
                Starter(osfor="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="لا"),
                Starter(meat="لا"),
                Starter(aadaas="نعم"),
                Starter(oninAndNanaAndZitAndKhbzAndWater="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="لا"),
                Starter(meat="لا"),
                Starter(aadaas="لا"),
                Starter(batata="نعم"),
                Starter(zit="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="لا"),
                Starter(meat="لا"),
                Starter(aadaas="لا"),
                Starter(batata="لا"),
                Starter(jaj="لا"),
            ),
            AND(
                Starter(bandora="لا"),
                Starter(bitnjan="لا"),
                Starter(laban="لا"),
                Starter(hmos="لا"),
                Starter(sh3iria="لا"),
                Starter(meat="لا"),
                Starter(aadaas="لا"),
                Starter(batata="لا"),
                Starter(jaj="نعم"),
                Starter(hbashatAlSizar="لا"),
            )
        )
    )
    def starter_rule_final(self):
        print("______________________________")
        print("لقد فرشت المقبلات    ")
        print("______________________________")
