from experta import *


class AnimalFood(Fact):
    pass


class AnimalFoodEngine(KnowledgeEngine):

    @DefFacts()
    def initial(self):
        print("\tالزيت او السمنة حسب الرغبة مع كافة الوجبات")
        yield AnimalFood(meat=input("هل لديك لحمة؟ ( نعم ، لا ) :: "))

    @Rule(AnimalFood(meat="نعم"))
    def animal_food_rule01(self):
        self.declare(AnimalFood(rise=input("هل لديك رز؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
        )
    )
    def animal_food_rule02(self):
        self.declare(AnimalFood(peas=input("هل لديك بازلاء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="نعم"),
        )
    )
    def animal_food_rule03(self):
        self.declare(AnimalFood(freaka=input("هل لديك فريكة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="نعم"),
            AnimalFood(freaka="نعم"),
        )
    )
    def animal_food_rule04(self):
        print("______________________________")
        print("الوجبة      : فريكة برز     ")
        print("يمكنك إضافة :    مكسرات     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="نعم"),
            AnimalFood(freaka="لا"),
        )
    )
    def animal_food_rule05(self):
        print("______________________________")
        print("الوجبة      : رز ببازيليا     ")
        print("يمكنك إضافة :      مكسرات     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
        )
    )
    def animal_food_rule06(self):
        self.declare(AnimalFood(fool=input("هل لديك فول؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="نعم"),
        )
    )
    def animal_food_rule07(self):
        print("______________________________")
        print("الوجبة      :     رز بفول     ")
        print("يمكنك إضافة :      مكسرات     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
        )
    )
    def animal_food_rule08(self):
        self.declare(AnimalFood(bitnjan=input("هل لديك بيتنجان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="نعم"),
        )
    )
    def animal_food_rule09(self):
        print("______________________________")
        print("الوجبة      :     مقلوبة     ")
        print("يمكنك إضافة :      مكسرات     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
        )
    )
    def animal_food_rule10(self):
        self.declare(AnimalFood(wrkEnb=input("هل لديك ورق عنب؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="نعم"),
        )
    )
    def animal_food_rule11(self):
        self.declare(AnimalFood(lemon=input("هل لديك ليمون؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="نعم"),
            AnimalFood(lemon="نعم"),
        )
    )
    def animal_food_rule12(self):
        self.declare(AnimalFood(osfor=input("هل لديك عصفر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="نعم"),
            AnimalFood(lemon="نعم"),
            AnimalFood(osfor="نعم"),
        )
    )
    def animal_food_rule13(self):
        print("______________________________")
        print("الوجبة      :     ورق عنب     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
        )
    )
    def animal_food_rule14(self):
        self.declare(AnimalFood(kosa=input("هل لديك كوسا؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="نعم"),
        )
    )
    def animal_food_rule15(self):
        self.declare(AnimalFood(osforAndKmonAndNaNa=input("هل لديك عصفر وكمون ونعنع؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="نعم"),
            AnimalFood(osforAndKmonAndNaNa="نعم"),
        )
    )
    def animal_food_rule16(self):
        self.declare(AnimalFood(rabAlBandora=input("هل لديك رب البندورة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="نعم"),
            AnimalFood(osforAndKmonAndNaNa="نعم"),
            AnimalFood(rabAlBandora="نعم"),
        )
    )
    def animal_food_rule17(self):
        print("______________________________")
        print("الوجبة      :     كوسا محشي     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
        )
    )
    def animal_food_rule18(self):
        self.declare(AnimalFood(bamia=input("هل لديك بامية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="نعم"),
        )
    )
    def animal_food_rule19(self):
        self.declare(AnimalFood(bndora=input("هل لديك بندورة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="نعم"),
            AnimalFood(bndora="نعم"),
        )
    )
    def animal_food_rule20(self):
        self.declare(AnimalFood(sh3ireah=input("هل لديك شعيرية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="نعم"),
            AnimalFood(bndora="نعم"),
            AnimalFood(sh3ireah="نعم"),
        )
    )
    def animal_food_rule21(self):
        self.declare(AnimalFood(rbAlbandora=input("هل لديك رب البندروة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="نعم"),
            AnimalFood(bndora="نعم"),
            AnimalFood(sh3ireah="نعم"),
            AnimalFood(rbAlbandora="نعم"),
        )
    )
    def animal_food_rule22(self):
        print("______________________________")
        print("الوجبة     :   بامية و رز     ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
        )
    )
    def animal_food_rule23(self):
        self.declare(AnimalFood(onin=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
        )
    )
    def animal_food_rule24(self):
        self.declare(AnimalFood(laban=input("هل لديك لبن؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(laban="نعم"),
        )
    )
    def animal_food_rule25(self):
        self.declare(AnimalFood(nashaaAndShearia=input("هل لديك نشاء وشعيرية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(laban="نعم"),
            AnimalFood(nashaaAndShearia="نعم"),
        )
    )
    def animal_food_rule26(self):
        print("______________________________")
        print("الوجبة     :   شاكرية و رز    ")
        print("______________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(laban="لا"),
        )
    )
    def animal_food_rule27(self):
        self.declare(AnimalFood(fasolia=input("هل لديك فاصولياء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(laban="لا"),
            AnimalFood(fasolia="نعم"),
        )
    )
    def animal_food_rule28(self):
        self.declare(AnimalFood(rbAlbandora=input("هل لديك  رب البندورة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(laban="لا"),
            AnimalFood(fasolia="نعم"),
            AnimalFood(rbAlbandora="نعم"),
        )
    )
    def animal_food_rule30(self):
        self.declare(AnimalFood(sh3ireah=input("هل لديك  شعيرية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(laban="لا"),
            AnimalFood(fasolia="نعم"),
            AnimalFood(rbAlbandora="نعم"),
            AnimalFood(sh3ireah="نعم"),
        )
    )
    def animal_food_rule31(self):
        print("_________________________________")
        print("الوجبة      :   فاصولياء و رز    ")
        print("يمكنك إضافة :        ثوم         ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
        )
    )
    def animal_food_rule32(self):
        self.declare(AnimalFood(malfof=input("هل لديك  ملفوف؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="نعم"),
        )
    )
    def animal_food_rule33(self):
        self.declare(AnimalFood(dhneh=input("هل لديك  دهنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="نعم"),
            AnimalFood(dhneh="نعم"),
        )
    )
    def animal_food_rule34(self):
        self.declare(AnimalFood(nanaAndKmonAndThom=input("هل لديك  نعنع وكمون وثوم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="نعم"),
            AnimalFood(dhneh="نعم"),
            AnimalFood(nanaAndKmonAndThom="نعم"),
        )
    )
    def animal_food_rule35(self):
        print("_________________________________")
        print("الوجبة      :       ملفوف        ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="لا"),
        )
    )
    def animal_food_rule36(self):
        self.declare(AnimalFood(anjinar=input("هل لديك  انغينار؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="لا"),
            AnimalFood(anjinar="نعم"),
        )
    )
    def animal_food_rule37(self):
        self.declare(AnimalFood(sh3ireah=input("هل لديك  شعيرية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="لا"),
            AnimalFood(anjinar="نعم"),
            AnimalFood(sh3ireah="نعم"),
        )
    )
    def animal_food_rule38(self):
        self.declare(AnimalFood(flfl=input("هل لديك  فلفل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="نعم"),
            AnimalFood(peas="لا"),
            AnimalFood(fool="لا"),
            AnimalFood(bitnjan="لا"),
            AnimalFood(wrkEnb="لا"),
            AnimalFood(kosa="لا"),
            AnimalFood(bamia="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(malfof="لا"),
            AnimalFood(anjinar="نعم"),
            AnimalFood(sh3ireah="نعم"),
            AnimalFood(flfl="نعم"),
        )
    )
    def animal_food_rule39(self):
        print("_________________________________")
        print("الوجبة      :       انغينار      ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
        )
    )
    def animal_food_rule40(self):
        self.declare(AnimalFood(kzbara=input("هل لديك كزبرة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
        )
    )
    def animal_food_rule41(self):
        self.declare(AnimalFood(mlokhieah=input("هل لديك ملوخية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
            AnimalFood(mlokhieah="نعم"),
        )
    )
    def animal_food_rule42(self):
        self.declare(AnimalFood(lemonAndThom=input("هل لديك ليمون وثوم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
            AnimalFood(mlokhieah="نعم"),
            AnimalFood(lemonAndThom="نعم"),
        )
    )
    def animal_food_rule43(self):
        print("_________________________________")
        print("الوجبة      :        ملوخية      ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
            AnimalFood(mlokhieah="لا"),
        )
    )
    def animal_food_rule44(self):
        self.declare(AnimalFood(agin=input("هل لديك عجين؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
            AnimalFood(mlokhieah="لا"),
            AnimalFood(agin="نعم"),
        )
    )
    def animal_food_rule45(self):
        self.declare(AnimalFood(oninAndThom=input("هل لديك بصل وثوم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
            AnimalFood(mlokhieah="لا"),
            AnimalFood(agin="نعم"),
            AnimalFood(oninAndThom="نعم"),
        )
    )
    def animal_food_rule46(self):
        self.declare(AnimalFood(labanAndNashaa=input("هل لديك لبن ونشاء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="نعم"),
            AnimalFood(mlokhieah="لا"),
            AnimalFood(agin="نعم"),
            AnimalFood(oninAndThom="نعم"),
            AnimalFood(labanAndNashaa="نعم"),
        )
    )
    def animal_food_rule47(self):
        print("_________________________________")
        print("الوجبة      :        شيش برك      ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
        )
    )
    def animal_food_rule48(self):
        self.declare(AnimalFood(brghl=input("هل لديك برغل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="نعم"),
        )
    )
    def animal_food_rule49(self):
        self.declare(AnimalFood(onin=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(onin="نعم"),
        )
    )
    def animal_food_rule50(self):
        self.declare(AnimalFood(dbsRman=input("هل لديك دبس رمان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(onin="نعم"),
            AnimalFood(dbsRman="نعم"),
        )
    )
    def animal_food_rule51(self):
        print("_________________________________")
        print("الوجبة      :     كبة مقلية      ")
        print("يمكنك إضافة : زيت للقلي ومكسرات  ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(onin="لا"),
        )
    )
    def animal_food_rule52(self):
        self.declare(AnimalFood(tarkhom=input("هل لديك طرخوم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(tarkhom="نعم"),
        )
    )
    def animal_food_rule53(self):
        self.declare(AnimalFood(labanAndNashaa=input("هل لديك لبن ونشاء؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(tarkhom="نعم"),
            AnimalFood(labanAndNashaa="نعم"),
        )
    )
    def animal_food_rule54(self):
        print("_________________________________")
        print("الوجبة      :     كبة لبنية      ")
        print("يمكنك إضافة : زيت للقلي ومكسرات  ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
        )
    )
    def animal_food_rule54_(self):
        self.declare(AnimalFood(onin=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(onin="نعم"),
        )
    )
    def animal_food_rule55(self):
        self.declare(AnimalFood(bandoraAndFlifla=input("هل لديك بندورة وفليفلة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(bandoraAndFlifla="نعم"),
        )
    )
    def animal_food_rule56(self):
        self.declare(AnimalFood(bitnjan=input("هل لديك بيتنجان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(bandoraAndFlifla="نعم"),
            AnimalFood(bitnjan="نعم"),
        )
    )
    def animal_food_rule57(self):
        print("_________________________________")
        print("الوجبة      :    منزلة بيتنجان   ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(onin="نعم"),
            AnimalFood(bandoraAndFlifla="نعم"),
            AnimalFood(bitnjan="لا"),
        )
    )
    def animal_food_rule58(self):
        print("_________________________________")
        print("الوجبة      :     كباب هندي      ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(onin="لا"),
        )
    )
    def animal_food_rule59(self):
        self.declare(AnimalFood(lemon=input("هل لديك ليمون؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="نعم"),
            AnimalFood(rise="لا"),
            AnimalFood(kzbara="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(onin="لا"),
            AnimalFood(lemon="نعم"),
        )
    )
    def animal_food_rule60(self):
        print("_________________________________")
        print("الوجبة      :   شرحات مطفاية     ")
        print("يمكنك إضافة :        فطر         ")
        print("_________________________________")

    @Rule(AnimalFood(meat="لا"))
    def animal_food_rule61(self):
        self.declare(AnimalFood(rise=input("هل لديك رز؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
        )
    )
    def animal_food_rule62(self):
        self.declare(AnimalFood(jaj=input("هل لديك دجاج؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
        )
    )
    def animal_food_rule63(self):
        self.declare(AnimalFood(bharat=input("هل لديك بهارات؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
        )
    )
    def animal_food_rule64(self):
        self.declare(AnimalFood(sh3ireah=input("هل لديك شعيرية؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="نعم"),
        )
    )
    def animal_food_rule65(self):
        self.declare(AnimalFood(osfor=input("هل لديك عصفر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="نعم"),
            AnimalFood(osfor="نعم"),
        )
    )
    def animal_food_rule66(self):
        print("_________________________________")
        print("الوجبة      :   رز وجاج     ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="لا"),
        )
    )
    def animal_food_rule67(self):
        self.declare(AnimalFood(bandora=input("هل لديك بندورة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="لا"),
            AnimalFood(bandora="نعم"),
        )
    )
    def animal_food_rule68(self):
        print("_________________________________")
        print("الوجبة      :       كبسة         ")
        print("يمكنك إضافة :   مكسرات وفليفلة   ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="لا"),
            AnimalFood(bandora="لا"),
        )
    )
    def animal_food_rule69(self):
        self.declare(AnimalFood(fhm=input("هل لديك فحم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="لا"),
            AnimalFood(bandora="لا"),
            AnimalFood(fhm="نعم"),
        )
    )
    def animal_food_rule70(self):
        self.declare(AnimalFood(molinat=input("هل لديك ملونات؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="لا"),
            AnimalFood(bandora="لا"),
            AnimalFood(fhm="نعم"),
            AnimalFood(molinat="نعم"),
        )
    )
    def animal_food_rule71(self):
        self.declare(AnimalFood(krnfulAndFlfl=input("هل لديك قرنفل وفلفل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="نعم"),
            AnimalFood(sh3ireah="لا"),
            AnimalFood(bandora="لا"),
            AnimalFood(fhm="نعم"),
            AnimalFood(molinat="نعم"),
            AnimalFood(krnfulAndFlfl="نعم"),
        )
    )
    def animal_food_rule72(self):
        print("_________________________________")
        print("الوجبة      :       مندي         ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="لا"),
        )
    )
    def animal_food_rule73(self):
        self.declare(AnimalFood(kashkawan=input("هل لديك قشقوان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="لا"),
            AnimalFood(kashkawan="نعم"),
        )
    )
    def animal_food_rule74(self):
        self.declare(AnimalFood(crema=input("هل لديك كريمة طبخ؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="لا"),
            AnimalFood(kashkawan="نعم"),
            AnimalFood(crema="نعم"),
        )
    )
    def animal_food_rule75(self):
        self.declare(AnimalFood(ftr=input("هل لديك فطر؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="نعم"),
            AnimalFood(jaj="نعم"),
            AnimalFood(bharat="لا"),
            AnimalFood(kashkawan="نعم"),
            AnimalFood(crema="نعم"),
            AnimalFood(ftr="نعم"),
        )
    )
    def animal_food_rule76(self):
        print("_________________________________")
        print("الوجبة      :     كوردون بلو     ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
        )
    )
    def animal_food_rule77(self):
        self.declare(AnimalFood(jaj=input("هل لديك دجاج؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
        )
    )
    def animal_food_rule78(self):
        self.declare(AnimalFood(onin=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="نعم"),
        )
    )
    def animal_food_rule79(self):
        self.declare(AnimalFood(smmak=input("هل لديك سماق؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="نعم"),
            AnimalFood(smmak="نعم"),
        )
    )
    def animal_food_rule80(self):
        self.declare(AnimalFood(khbz=input("هل لديك خبز؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="نعم"),
            AnimalFood(smmak="نعم"),
            AnimalFood(khbz="نعم"),
        )
    )
    def animal_food_rule81(self):
        print("_________________________________")
        print("الوجبة     :        مسخن         ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="نعم"),
            AnimalFood(smmak="لا"),
        )
    )
    def animal_food_rule82(self):
        self.declare(AnimalFood(cremaa=input("هل لديك كريمة(حليب، زبدة, طحين)؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="نعم"),
            AnimalFood(smmak="لا"),
            AnimalFood(cremaa="نعم"),
        )
    )
    def animal_food_rule83(self):
        print("_________________________________")
        print("الوجبة     :   جاج بالكريمة      ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
        )
    )
    def animal_food_rule84(self):
        self.declare(AnimalFood(brghl=input("هل لديك برغل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(brghl="نعم"),
        )
    )
    def animal_food_rule85(self):
        self.declare(AnimalFood(laban=input("هل لديك لبن؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(laban="نعم"),
        )
    )
    def animal_food_rule86(self):
        self.declare(AnimalFood(bharat=input("هل لديك بهارات؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(brghl="نعم"),
            AnimalFood(laban="نعم"),
            AnimalFood(bharat="نعم"),
        )
    )
    def animal_food_rule87(self):
        print("_________________________________")
        print("الوجبة     :        مليحي        ")
        print("_________________________________")

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(brghl="لا"),
        )
    )
    def animal_food_rule88(self):
        self.declare(AnimalFood(agin=input("هل لديك عجين؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(agin="نعم"),
        )
    )
    def animal_food_rule89(self):
        self.declare(AnimalFood(flifla=input("هل لديك فليفلة؟ ( نعم ، لا ) :: ")))
        self.declare(AnimalFood(maunez=input("هل لديك ميونيز؟ ( نعم ، لا ) :: ")))
        self.declare(AnimalFood(btata=input("هل لديك بطاطا؟  ( نعم ، لا ) :: ")))
        self.declare(AnimalFood(kashkawan=input("هل لديك قشقوان؟ ( نعم ، لا ) :: ")))
        self.declare(AnimalFood(jzr=input("هل لديك جزر؟    ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            AnimalFood(meat="لا"),
            AnimalFood(rise="لا"),
            AnimalFood(jaj="نعم"),
            AnimalFood(onin="لا"),
            AnimalFood(brghl="لا"),
            AnimalFood(agin="نعم"),
            AnimalFood(flifla="نعم"),
            AnimalFood(maunez="نعم"),
            AnimalFood(btata="نعم"),
            AnimalFood(kashkawan="نعم"),
            AnimalFood(jzr="نعم"),
        )
    )
    def animal_food_rule90(self):
        print("_________________________________")
        print("الوجبة     :     جيب التاجر      ")
        print("_________________________________")

    @Rule(
        OR(
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="نعم"),
                AnimalFood(lemon="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="نعم"),
                AnimalFood(lemon="نعم"),
                AnimalFood(osfor="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="نعم"),
                AnimalFood(osforAndKmonAndNaNa="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="نعم"),
                AnimalFood(osforAndKmonAndNaNa="نعم"),
                AnimalFood(rabAlBandora="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="نعم"),
                AnimalFood(bndora="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="نعم"),
                AnimalFood(bndora="نعم"),
                AnimalFood(sh3ireah="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="نعم"),
                AnimalFood(bndora="نعم"),
                AnimalFood(sh3ireah="نعم"),
                AnimalFood(rbAlbandora="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="نعم"),
                AnimalFood(laban="نعم"),
                AnimalFood(nashaaAndShearia="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="نعم"),
                AnimalFood(laban="لا"),
                AnimalFood(fasolia="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="نعم"),
                AnimalFood(laban="لا"),
                AnimalFood(fasolia="نعم"),
                AnimalFood(rbAlbandora="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="نعم"),
                AnimalFood(laban="لا"),
                AnimalFood(fasolia="نعم"),
                AnimalFood(rbAlbandora="نعم"),
                AnimalFood(sh3ireah="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(malfof="نعم"),
                AnimalFood(dhneh="لا"),
            ),

            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(malfof="نعم"),
                AnimalFood(dhneh="نعم"),
                AnimalFood(nanaAndKmonAndThom="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(malfof="لا"),
                AnimalFood(anjinar="نعم"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(malfof="لا"),
                AnimalFood(anjinar="نعم"),
                AnimalFood(sh3ireah="نعم"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="نعم"),
                AnimalFood(peas="لا"),
                AnimalFood(fool="لا"),
                AnimalFood(bitnjan="لا"),
                AnimalFood(wrkEnb="لا"),
                AnimalFood(kosa="لا"),
                AnimalFood(bamia="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(malfof="لا"),
                AnimalFood(anjinar="نعم"),
                AnimalFood(sh3ireah="نعم"),
                AnimalFood(flfl="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="نعم"),
                AnimalFood(mlokhieah="نعم"),
                AnimalFood(lemonAndThom="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="نعم"),
                AnimalFood(mlokhieah="لا"),
                AnimalFood(agin="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="نعم"),
                AnimalFood(mlokhieah="لا"),
                AnimalFood(agin="نعم"),
                AnimalFood(oninAndThom="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="نعم"),
                AnimalFood(mlokhieah="لا"),
                AnimalFood(agin="نعم"),
                AnimalFood(oninAndThom="نعم"),
                AnimalFood(labanAndNashaa="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="لا"),
                AnimalFood(brghl="نعم"),
                AnimalFood(onin="نعم"),
                AnimalFood(dbsRman="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="لا"),
                AnimalFood(brghl="نعم"),
                AnimalFood(onin="لا"),
                AnimalFood(tarkhom="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="لا"),
                AnimalFood(brghl="نعم"),
                AnimalFood(onin="لا"),
                AnimalFood(tarkhom="نعم"),
                AnimalFood(labanAndNashaa="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="لا"),
                AnimalFood(brghl="لا"),
                AnimalFood(onin="نعم"),
                AnimalFood(bandoraAndFlifla="لا"),
            ),
            AND(
                AnimalFood(meat="نعم"),
                AnimalFood(rise="لا"),
                AnimalFood(kzbara="لا"),
                AnimalFood(brghl="لا"),
                AnimalFood(onin="لا"),
                AnimalFood(lemon="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="نعم"),
                AnimalFood(sh3ireah="نعم"),
                AnimalFood(osfor="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="نعم"),
                AnimalFood(sh3ireah="لا"),
                AnimalFood(bandora="لا"),
                AnimalFood(fhm="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="نعم"),
                AnimalFood(sh3ireah="لا"),
                AnimalFood(bandora="لا"),
                AnimalFood(fhm="نعم"),
                AnimalFood(molinat="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="نعم"),
                AnimalFood(sh3ireah="لا"),
                AnimalFood(bandora="لا"),
                AnimalFood(fhm="نعم"),
                AnimalFood(molinat="نعم"),
                AnimalFood(krnfulAndFlfl="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="لا"),
                AnimalFood(kashkawan="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="لا"),
                AnimalFood(kashkawan="نعم"),
                AnimalFood(crema="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="نعم"),
                AnimalFood(jaj="نعم"),
                AnimalFood(bharat="لا"),
                AnimalFood(kashkawan="نعم"),
                AnimalFood(crema="نعم"),
                AnimalFood(ftr="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="نعم"),
                AnimalFood(onin="نعم"),
                AnimalFood(smmak="نعم"),
                AnimalFood(khbz="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="نعم"),
                AnimalFood(onin="نعم"),
                AnimalFood(smmak="لا"),
                AnimalFood(cremaa="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="نعم"),
                AnimalFood(onin="لا"),
                AnimalFood(brghl="نعم"),
                AnimalFood(laban="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="نعم"),
                AnimalFood(onin="لا"),
                AnimalFood(brghl="نعم"),
                AnimalFood(laban="نعم"),
                AnimalFood(bharat="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="نعم"),
                AnimalFood(onin="لا"),
                AnimalFood(brghl="لا"),
                AnimalFood(agin="لا"),
            ),
            AND(
                AnimalFood(meat="لا"),
                AnimalFood(rise="لا"),
                AnimalFood(jaj="نعم"),
                AnimalFood(onin="لا"),
                AnimalFood(brghl="لا"),
                AnimalFood(agin="نعم"),
                OR(
                    AnimalFood(flifla="لا"),
                    AnimalFood(maunez="لا"),
                    AnimalFood(btata="لا"),
                    AnimalFood(kashkawan="لا"),
                    AnimalFood(jzr="لا"),
                )
            )

        )
    )
    def animal_food_rule_final(self):
        print("_________________________________")
        print("\t\tقم بإعادة طلب الطعام الحيواني       ")
        print("_________________________________")
