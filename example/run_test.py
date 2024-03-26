import bt4vt

score_file = "~/bias_tests_4_voice_tech/example/resnetse34v2_H-eval_scores.csv"
config_file = "~/bias_tests_4_voice_tech/example/config.yaml"

test = bt4vt.core.SpeakerBiasTest(score_file, config_file)

test.run_tests()
