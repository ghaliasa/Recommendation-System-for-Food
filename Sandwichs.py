from experta import *


class Sandwiches(Fact):
    pass


class SandwichesEngine(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Sandwiches(meat_chicken=input("هل لديك لحمة أم دجاج؟ ( لحمة ، دجاج ) :: "))

    @Rule(Sandwiches(meat_chicken="دجاج"))
    def sandwiches_rule01(self):
        self.declare(Sandwiches(type=input(
            "ما نوع الدجاج لديك؟ ( شرحات ، فتايل ، مفروم، فتايل شاورما ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
        )
    )
    def sandwiches_rule02(self):
        self.declare(Sandwiches(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
        )
    )
    def sandwiches_rule03(self):
        self.declare(Sandwiches(flour=input("هل لديك طحين؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
        )
    )
    def sandwiches_rule04(self):
        self.declare(Sandwiches(zwieback=input(
            "هل لديك بقسماط؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
        )
    )
    def sandwiches_rule05(self):
        self.declare(Sandwiches(escalope_spices=input(
            "هل لديك بهارات اسكالوب؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
            Sandwiches(escalope_spices="نعم"),
        )
    )
    def pastries_rule06(self):
        print("_______________________________________________")
        print("           الوجبة        :             اسكالوب")
        print(" يمكنك إضافة :  يفضًل وجود خبز صمون، مايونيز  ")
        print("________________________________________________")

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
            Sandwiches(escalope_spices="لا"),
        )
    )
    def sandwiches_rule07(self):
        self.declare(Sandwiches(kashkawan=input(
            "هل لديك قشقوان؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
            Sandwiches(escalope_spices="لا"),
            Sandwiches(kashkawan="نعم"),
        )
    )
    def sandwiches_rule08(self):
        self.declare(Sandwiches(soprem_spices=input(
            "هل لديك بهارات سوبريم؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="شرحات"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
            Sandwiches(escalope_spices="لا"),
            Sandwiches(kashkawan="نعم"),
            Sandwiches(soprem_spices="نعم"),
        )
    )
    def sandwiches_rule09(self):
        print("_____________________________________________________")
        print("            الوجبة    :                    سوبريم   ")
        print(" يمكنك إضافة :  يفضًل وجود خبز صمون ، فطر، مايونيز ")
        print("______________________________________________________")

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل"),
        )
    )
    def sandwiches_rule10(self):
        self.declare(Sandwiches(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل"),
            Sandwiches(egg="نعم"),
        )
    )
    def sandwiches_rule11(self):
        self.declare(Sandwiches(flour=input("هل لديك طحين؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
        )
    )
    def sandwiches_rule12(self):
        self.declare(Sandwiches(zwieback=input(
            "هل لديك بقسماط؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
        )
    )
    def sandwiches_rule13(self):
        self.declare(Sandwiches(krespe_spices=input(
            "هل لديك بهارات كرسبي؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل"),
            Sandwiches(egg="نعم"),
            Sandwiches(flour="نعم"),
            Sandwiches(zwieback="نعم"),
            Sandwiches(krespe_spices="نعم"),

        )
    )
    def sandwiches_rule14(self):
        print("________________________________________________")
        print("             الوجبة       :              كرسبي")
        print(" يمكنك إضافة :  يفضًل وجود خبز صمون، مايونيز  ")
        print("________________________________________________")

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="مفروم"),
        )
    )
    def sandwiches_rule15(self):
        self.declare(Sandwiches(egg=input("هل لديك بيض؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="مفروم"),
            Sandwiches(egg="نعم"),
        )
    )
    def sandwiches_rule16(self):
        self.declare(Sandwiches(piece_of_fat=input(
            "هل لديك دهنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="مفروم"),
            Sandwiches(egg="نعم"),
            Sandwiches(piece_of_fat="نعم"),
        )
    )
    def sandwiches_rule17(self):
        self.declare(Sandwiches(tomato=input(
            "هل لديك بندورة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="مفروم"),
            Sandwiches(egg="نعم"),
            Sandwiches(piece_of_fat="نعم"),
            Sandwiches(tomato="نعم"),
        )
    )
    def sandwiches_rule18(self):
        print("______________________________________________________")
        print("          الوجبة      :                    برغر دجاج ")
        print(" يمكنك إضافة :  يفضًل وجود خبز مدور ، مخلل، مايونيز ")
        print("_______________________________________________________")

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل شاورما"),
        )
    )
    def sandwiches_rule19(self):
        print("البهارات المشكلة: كزبرة يابسة، زنجبيل، قرفة، هيل، قرنفل، جوزة الطيب ")
        self.declare(Sandwiches(spices=input(
            "هل لديك بهارات مشكلة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل شاورما"),
            Sandwiches(spices="نعم"),
        )
    )
    def sandwiches_rule20(self):
        self.declare(Sandwiches(lemon=input("هل لديك ليمون؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل شاورما"),
            Sandwiches(spices="نعم"),
            Sandwiches(lemon="نعم"),
        )
    )
    def sandwiches_rule21(self):
        self.declare(Sandwiches(mayouniz=input(
            "هل لديك مايونيز؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل شاورما"),
            Sandwiches(spices="نعم"),
            Sandwiches(lemon="نعم"),
            Sandwiches(mayouniz="نعم"),
        )
    )
    def sandwiches_rule22(self):
        self.declare(Sandwiches(capsicum_molasses=input(
            "هل لديك دبس فليفلة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="دجاج"),
            Sandwiches(type="فتايل شاورما"),
            Sandwiches(spices="نعم"),
            Sandwiches(lemon="نعم"),
            Sandwiches(mayouniz="نعم"),
            Sandwiches(capsicum_molasses="نعم"),
        )
    )
    def sandwiches_rule23(self):
        print("______________________________________________________")
        print("           الوجبة     :                شاورما دجاج ")
        print("      ،يمكنك إضافة :  يفضًل وجود خبز سياحي أو مشروح ")
        print("                مخلل، مايونيز                        ")
        print("_______________________________________________________")

    @Rule(Sandwiches(meat_chicken="لحمة"))
    def sandwiches_rule24(self):
        self.declare(Sandwiches(type=input(
            "ما نوع اللحمة لديك ؟ ( لحمة شاروما ، لحمة مفرومة ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة شاورما"),
        )
    )
    def sandwiches_rule25(self):
        self.declare(Sandwiches(yogurt=input("هل لديك لبن؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة شاورما"),
            Sandwiches(yogurt="نعم"),
        )
    )
    def sandwiches_rule26(self):
        self.declare(Sandwiches(piece_of_fat=input(
            "هل لديك دهنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة شاورما"),
            Sandwiches(yogurt="نعم"),
            Sandwiches(piece_of_fat="نعم"),
        )
    )
    def sandwiches_rule27(self):
        self.declare(Sandwiches(lemon=input("هل لديك ليمون؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة شاورما"),
            Sandwiches(yogurt="نعم"),
            Sandwiches(piece_of_fat="نعم"),
            Sandwiches(lemon="نعم"),
        )
    )
    def sandwiches_rule28(self):
        self.declare(Sandwiches(shawrma_spices=input(
            "هل لديك بهارات شاورما؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة شاورما"),
            Sandwiches(yogurt="نعم"),
            Sandwiches(piece_of_fat="نعم"),
            Sandwiches(lemon="نعم"),
            Sandwiches(shawrma_spices="نعم"),
        )
    )
    def sandwiches_rule29(self):
        print("______________________________________________________")
        print("           الوجبة     :                شاورما لحمة ")
        print("      ،يمكنك إضافة :  يفضًل وجود خبز سياحي أو مشروح ")
        print("                      بصل                             ")
        print("_______________________________________________________")

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة مفرومة"),
        )
    )
    def sandwiches_rule30(self):
        self.declare(Sandwiches(piece_of_fat=input(
            "هل لديك دهنة؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة مفرومة"),
            Sandwiches(piece_of_fat="نعم"),
        )
    )
    def sandwiches_rule31(self):
        self.declare(Sandwiches(onion=input("هل لديك بصل؟ ( نعم ، لا ) :: ")))

    @Rule(
        AND(
            Sandwiches(meat_chicken="لحمة"),
            Sandwiches(type="لحمة مفرومة"),
            Sandwiches(piece_of_fat="نعم"),
            Sandwiches(onion="نعم"),
        )
    )
    def sandwiches_rule32(self):
        print("__________________________________________________________")
        print("          الوجبة      :                        برغر لحمة ")
        print(" يمكنك إضافة :  يفضًل وجود خبز مدور ، مخلل، بيض، بندورة ")
        print("___________________________________________________________")

    @Rule(
        OR(
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="شرحات"),
                Sandwiches(egg="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="شرحات"),
                Sandwiches(egg="نعم"),
                Sandwiches(flour="نعم"),
                Sandwiches(zwieback="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="فتايل"),
                Sandwiches(egg="نعم"),
                Sandwiches(flour="نعم"),
                Sandwiches(zwieback="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="مفروم"),
                Sandwiches(egg="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="مفروم"),
                Sandwiches(egg="نعم"),
                Sandwiches(piece_of_fat="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="مفروم"),
                Sandwiches(egg="نعم"),
                Sandwiches(piece_of_fat="نعم"),
                Sandwiches(tomato="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="شرحات"),
                Sandwiches(egg="نعم"),
                Sandwiches(flour="نعم"),
                Sandwiches(zwieback="نعم"),
                Sandwiches(escalope_spices="لا"),
                Sandwiches(kashkawan="لا"),
                Sandwiches(soprem_spices="نعم"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="شرحات"),
                Sandwiches(egg="نعم"),
                Sandwiches(flour="نعم"),
                Sandwiches(zwieback="نعم"),
                Sandwiches(escalope_spices="لا"),
                Sandwiches(kashkawan="نعم"),
                Sandwiches(soprem_spices="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="فتايل"),
                Sandwiches(egg="نعم"),
                Sandwiches(flour="نعم"),
                Sandwiches(zwieback="نعم"),
                Sandwiches(krespe_spices="لا"),

            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="فتايل شاورما"),
                Sandwiches(spices="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="فتايل شاورما"),
                Sandwiches(spices="نعم"),
                Sandwiches(lemon="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="فتايل شاورما"),
                Sandwiches(spices="نعم"),
                Sandwiches(lemon="نعم"),
                Sandwiches(mayouniz="لا"),
                Sandwiches(capsicum_molasses="نعم"),
            ),
            AND(
                Sandwiches(meat_chicken="دجاج"),
                Sandwiches(type="فتايل شاورما"),
                Sandwiches(spices="نعم"),
                Sandwiches(lemon="نعم"),
                Sandwiches(mayouniz="نعم"),
                Sandwiches(capsicum_molasses="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="لحمة"),
                Sandwiches(type="لحمة شاورما"),
                Sandwiches(yogurt="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="لحمة"),
                Sandwiches(type="لحمة شاورما"),
                Sandwiches(yogurt="نعم"),
                Sandwiches(piece_of_fat="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="لحمة"),
                Sandwiches(type="لحمة شاورما"),
                Sandwiches(yogurt="نعم"),
                Sandwiches(piece_of_fat="نعم"),
                Sandwiches(lemon="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="لحمة"),
                Sandwiches(type="لحمة شاورما"),
                Sandwiches(yogurt="نعم"),
                Sandwiches(piece_of_fat="نعم"),
                Sandwiches(lemon="نعم"),
                Sandwiches(shawrma_spices="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="لحمة"),
                Sandwiches(type="لحمة مفرومة"),
                Sandwiches(piece_of_fat="لا"),
            ),
            AND(
                Sandwiches(meat_chicken="لحمة"),
                Sandwiches(type="لحمة مفرومة"),
                Sandwiches(piece_of_fat="نعم"),
                Sandwiches(onion="لا"),
            ),
        )
    )
    def sandwiches_rule33(self):
        print("______________________________")
        print("    قم بإعادة طلب السندويش  ")
        print("______________________________")
