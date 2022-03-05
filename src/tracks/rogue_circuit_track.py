#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class RogueCircuitTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Rogue Circuit"
        self._ui_description = "Named in honor of the 2021 DeepRacer Championship Cup winner, Sairam Naragoni, the Rogue Circuit is a short track (48.06m) features a variety of moderate curves and sweeping turns."
        self._ui_length_in_m = 48.06  # metres     (NOT STATED)
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_march_open"
        self._track_sector_dividers = [46, 100]
        self._annotations = config.rogue_circuit_annotations
        self._track_width = 1.067

        self._track_waypoints = [(-2.0369359850883484, -5.943336009979248), (-1.738064467906952, -5.989463567733765),
                                 (-1.4393694996833801, -6.0367231369018555), (-1.1408880352973938, -6.085307598114014),
                                 (-0.8426246047019958, -6.135216951370239), (-0.5444198995828629, -6.185476541519165),
                                 (-0.2462899014353752, -6.236176490783691), (0.051524948328733444, -6.288690090179443),
                                 (0.3483338952064514, -6.346576452255249), (0.6436918079853058, -6.411493539810181),
                                 (0.9376374185085297, -6.482528448104858), (1.2304140329360962, -6.5582499504089355),
                                 (1.5257545113563538, -6.62269401550293), (1.8273234963417053, -6.6392905712127686),
                                 (2.1288928985595703, -6.618226051330566), (2.4260480403900146, -6.563058614730835),
                                 (2.7137099504470825, -6.470383882522583), (2.9867550134658813, -6.340842008590698),
                                 (3.2398234605789185, -6.175666332244873), (3.4722654819488525, -5.982369661331177),
                                 (3.693007469177246, -5.7756829261779785), (3.904446840286255, -5.559537410736084),
                                 (4.102475523948669, -5.331040382385254), (4.286980986595154, -5.091476917266846),
                                 (4.4685304164886475, -4.849627494812012), (4.6437458992004395, -4.603174448013306),
                                 (4.799426555633545, -4.344087600708008), (4.9133594036102295, -4.064393043518066),
                                 (4.9756760597229, -3.768771529197693), (4.990587472915649, -3.466975450515747),
                                 (4.966310501098633, -3.165669083595276), (4.918224096298218, -2.8671375513076782),
                                 (4.859284400939941, -2.570557475090027), (4.777156829833984, -2.279561996459961),
                                 (4.701304912567139, -1.9868600368499756), (4.636876106262207, -1.6913945078849792),
                                 (4.5772013664245605, -1.3949394822120667), (4.535637140274048, -1.09552800655365),
                                 (4.543611526489258, -0.7937583029270172), (4.607089042663574, -0.49833714962005615),
                                 (4.716185092926025, -0.21654874039813876), (4.864802122116089, 0.04658450186252594),
                                 (5.0469725131988525, 0.2877318002283573), (5.259093523025513, 0.5029039569199085),
                                 (5.259093523025513, 0.5029039569199085), (5.501067399978638, 0.68390753865242),
                                 (5.7621095180511475, 0.8364308476448059), (6.030410528182983, 0.9759470522403717),
                                 (6.3061418533325195, 1.0999865233898163), (6.591607570648193, 1.1995515525341034),
                                 (6.881825923919678, 1.2845369279384613), (7.158332347869873, 1.4054960906505585),
                                 (7.401469945907593, 1.584732472896576), (7.61121392250061, 1.8022159934043884),
                                 (7.785490274429321, 2.0490845441818237), (7.923514366149902, 2.3179259300231934),
                                 (8.023163080215454, 2.6032029390335083), (8.080552339553833, 2.899960517883301),
                                 (8.094262838363647, 3.2018975019454956), (8.066569089889526, 3.5028750896453857),
                                 (8.001795530319214, 3.7981364727020264), (7.9055304527282715, 4.084710478782654),
                                 (7.7861008644104, 4.362487554550171), (7.640097379684448, 4.627154588699341),
                                 (7.465439081192017, 4.873879671096802), (7.268836498260499, 5.103580951690673),
                                 (7.060459852218628, 5.3227269649505615), (6.847865343093871, 5.5377869606018075),
                                 (6.625417470932007, 5.742587089538574), (6.38864803314209, 5.930606126785278),
                                 (6.136788606643677, 6.097854375839233), (5.870970010757446, 6.241891384124756),
                                 (5.5932300090789795, 6.361319065093994), (5.305620431900024, 6.454447984695435),
                                 (5.010941505432129, 6.522075414657593), (4.7127039432525635, 6.572042465209961),
                                 (4.412917375564575, 6.61158561706543), (4.111389875411987, 6.634212017059326),
                                 (3.8090630769729614, 6.639834403991699), (3.506811022758484, 6.630667686462402),
                                 (3.204898953437805, 6.6133339405059814), (2.9031169414520264, 6.593855381011963),
                                 (2.601729989051819, 6.569056510925293), (2.301701545715332, 6.531422138214111),
                                 (2.0059205293655378, 6.468984127044677), (1.721157550811766, 6.367913961410522),
                                 (1.4560169577598558, 6.222998619079589), (1.2288108468055725, 6.025204420089722),
                                 (1.0323731005191792, 5.795286893844604), (0.8291173726320267, 5.571383476257324),
                                 (0.6197642162442207, 5.3531599044799805), (0.40789822209626614, 5.137371540069582),
                                 (0.19429956376552582, 4.923299312591553), (-0.023909807205200195, 4.713939905166626),
                                 (-0.2506375387310982, 4.513866901397705), (-0.48888780921697617, 4.327690601348877),
                                 (-0.7386728525161743, 4.157300591468811), (-0.9981980323791504, 4.00212287902832),
                                 (-1.265850007534027, 3.861425995826721), (-1.540815532207489, 3.73561954498291),
                                 (-1.8222485184669495, 3.6250386238098145), (-2.1093080639839172, 3.530017375946045),
                                 (-2.401389002799988, 3.45179545879364), (-2.697199583053589, 3.3890894651412964),
                                 (-2.995718002319336, 3.3408654928207397), (-3.2961915731430054, 3.306867003440857),
                                 (-3.5979559421539307, 3.2873164415359497), (-3.900317072868347, 3.2859150171279907),
                                 (-4.201757431030273, 3.30913245677948), (-4.501722574234009, 3.3475000858306885),
                                 (-4.803642988204956, 3.360534429550171), (-5.104934930801392, 3.335668444633484),
                                 (-5.4039366245269775, 3.2906545400619507), (-5.698654651641846, 3.2232314348220825),
                                 (-5.985719680786133, 3.1284295320510864), (-6.2612550258636475, 3.004058003425598),
                                 (-6.521104574203491, 2.849557399749756), (-6.761330842971802, 2.6660499572753906),
                                 (-6.978301525115967, 2.4555970430374146), (-7.168851852416992, 2.2209489941596985),
                                 (-7.333338975906372, 1.9673035144805908), (-7.476794481277466, 1.701131522655487),
                                 (-7.608717441558838, 1.4290199875831604), (-7.726512908935547, 1.1505467295646667),
                                 (-7.82514500617981, 0.8647176027297974), (-7.905004262924194, 0.5730820894241333),
                                 (-7.967764854431152, 0.27728550136089325), (-8.017833709716797, -0.020941782742738724),
                                 (-8.057097673416138, -0.32076960802078247), (-8.082846403121948, -0.6220587491989136),
                                 (-8.09486985206604, -0.9242066740989657), (-8.093004941940308, -1.2265869975090027),
                                 (-8.080519199371338, -1.5287280082702637), (-8.055050611495972, -1.8300365209579468),
                                 (-8.013290405273438, -2.129516959190372), (-7.954392671585083, -2.426103949546814),
                                 (-7.878217458724976, -2.718727946281433), (-7.788170099258423, -3.007396936416626),
                                 (-7.681349277496336, -3.2902565002441437), (-7.555041313171385, -3.5649654865264924),
                                 (-7.4097075462341335, -3.8301074504852255), (-7.250068664550781, -4.086897611618042),
                                 (-7.071657419204714, -4.330975055694577), (-6.87251162528992, -4.558440446853634),
                                 (-6.653365612030029, -4.76670503616333), (-6.415413618087766, -4.95312547683716),
                                 (-6.161219596862789, -5.116795778274538), (-5.894645929336548, -5.259450912475586),
                                 (-5.617578506469727, -5.380439519882202), (-5.328897953033451, -5.469967603683471),
                                 (-5.03255558013916, -5.529980421066284), (-4.733617067337036, -5.5756354331970215),
                                 (-4.433925628662109, -5.616093158721924), (-4.134026527404785, -5.65498685836792),
                                 (-3.8341100215911865, -5.693745136260986), (-3.5342825651168823, -5.7331860065460205),
                                 (-3.2345045804977417, -5.772996425628662), (-2.9348185062408447, -5.813499450683594),
                                 (-2.635298490524292, -5.8552086353302), (-2.3359915018081665, -5.898420095443726),
                                 (-2.0369359850883484, -5.943336009979248)]
