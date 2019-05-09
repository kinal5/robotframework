
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARGUMENT ARGUMENTS ASSIGN COMMENT_HEADER DATA DEFAULT_TAGS DOCUMENTATION END EOS ERROR FOR FORCE_TAGS FOR_SEPARATOR KEYWORD KEYWORD_HEADER LIBRARY METADATA NAME NON_DATA_TOKENS OLD_FOR_INDENT RESOURCE RETURN SETTING_HEADER SETUP SUITE_SETUP SUITE_TEARDOWN TAGS TEARDOWN TEMPLATE TESTCASE_HEADER TEST_SETUP TEST_TEARDOWN TEST_TEMPLATE TEST_TIMEOUT TIMEOUT VARIABLE VARIABLES VARIABLE_HEADERdatafile :\n                    | sectionssections : section\n                    | sections sectionsection : setting_section\n                   | variable_section\n                   | testcase_section\n                   | keyword_section\n        setting_section : SETTING_HEADER EOS\n                           | SETTING_HEADER EOS settingssettings : setting\n                    | settings settingsetting : documentation_setting\n                   | suite_setup_setting EOS\n                   | suite_teardown_setting EOS\n                   | metadata_setting EOS\n                   | test_setup_setting EOS\n                   | test_teardown_setting EOS\n                   | test_template_setting EOS\n                   | test_timeout_setting EOS\n                   | force_tags_setting EOS\n                   | default_tags_setting EOS\n                   | library_setting EOS\n                   | resource_setting EOS\n                   | variables_setting EOS\n                   | setup_setting EOS\n                   | teardown_setting EOS\n                   | template_setting EOS\n                   | timeout_setting EOS\n                   | tags_setting EOS\n                   | arguments_setting EOS\n                   | return_setting EOSdocumentation_setting : DOCUMENTATION arguments EOSsuite_setup_setting : SUITE_SETUP argumentssuite_teardown_setting : SUITE_TEARDOWN argumentsmetadata_setting : METADATA argumentstest_setup_setting : TEST_SETUP argumentstest_teardown_setting : TEST_TEARDOWN argumentstest_template_setting : TEST_TEMPLATE argumentstest_timeout_setting : TEST_TIMEOUT argumentsforce_tags_setting : FORCE_TAGS argumentsdefault_tags_setting : DEFAULT_TAGS argumentslibrary_setting : LIBRARY argumentsresource_setting : RESOURCE argumentsvariables_setting : VARIABLES argumentssetup_setting : SETUP argumentsteardown_setting : TEARDOWN argumentstemplate_setting : TEMPLATE argumentstimeout_setting : TIMEOUT argumentstags_setting : TAGS argumentsarguments_setting : ARGUMENTS argumentsreturn_setting : RETURN argumentsvariable_section : VARIABLE_HEADER EOS\n                            | VARIABLE_HEADER EOS variablesvariables : variable\n                     | variables variablevariable : VARIABLE arguments EOStestcase_section : TESTCASE_HEADER EOS\n                            | TESTCASE_HEADER EOS testskeyword_section : KEYWORD_HEADER EOS\n                           | KEYWORD_HEADER EOS keywordstests : test\n                | tests testkeywords : keyword\n                    | keywords keywordtest : NAME EOS\n               | NAME EOS body_itemskeyword : NAME EOS\n                    | NAME EOS body_itemsbody_items : body_item\n                      | body_items body_item\n        body_item : forloop\n                     | setting\n                     | step\n                     | templatearguments\n                     | invalid_forloop\n        step : KEYWORD arguments EOSstep : assignments EOS\n                | assignments KEYWORD arguments EOSforloop : for_header for_body END EOS\n                   | for_header END EOS\n                   | END EOSfor_header : FOR arguments FOR_SEPARATOR arguments EOS\n                      | FOR arguments EOSfor_body : step\n                    | for_body step\n                    | templatearguments\n                    | for_body templatearguments\n        templatearguments : arguments EOSinvalid_forloop : for_header for_bodyassignments : ASSIGN\n                       | assignments ASSIGNarguments : args\n                     | empty_arg\n        args : ARGUMENT\n                | arguments ARGUMENTempty_arg : '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,12,13,14,15,16,17,18,19,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,111,113,114,115,116,117,119,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[-1,0,-2,-3,-5,-6,-7,-8,-4,-9,-53,-58,-60,-10,-11,-13,-54,-55,-59,-62,-61,-64,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-56,-63,-66,-65,-68,-33,-57,-67,-70,-72,-73,-74,-75,-76,-69,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'SETTING_HEADER':([0,2,3,4,5,6,7,12,13,14,15,16,17,18,19,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,111,113,114,115,116,117,119,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[8,8,-3,-5,-6,-7,-8,-4,-9,-53,-58,-60,-10,-11,-13,-54,-55,-59,-62,-61,-64,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-56,-63,-66,-65,-68,-33,-57,-67,-70,-72,-73,-74,-75,-76,-69,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'VARIABLE_HEADER':([0,2,3,4,5,6,7,12,13,14,15,16,17,18,19,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,111,113,114,115,116,117,119,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[9,9,-3,-5,-6,-7,-8,-4,-9,-53,-58,-60,-10,-11,-13,-54,-55,-59,-62,-61,-64,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-56,-63,-66,-65,-68,-33,-57,-67,-70,-72,-73,-74,-75,-76,-69,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TESTCASE_HEADER':([0,2,3,4,5,6,7,12,13,14,15,16,17,18,19,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,111,113,114,115,116,117,119,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[10,10,-3,-5,-6,-7,-8,-4,-9,-53,-58,-60,-10,-11,-13,-54,-55,-59,-62,-61,-64,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-56,-63,-66,-65,-68,-33,-57,-67,-70,-72,-73,-74,-75,-76,-69,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'KEYWORD_HEADER':([0,2,3,4,5,6,7,12,13,14,15,16,17,18,19,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,111,113,114,115,116,117,119,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[11,11,-3,-5,-6,-7,-8,-4,-9,-53,-58,-60,-10,-11,-13,-54,-55,-59,-62,-61,-64,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-56,-63,-66,-65,-68,-33,-57,-67,-70,-72,-73,-74,-75,-76,-69,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'EOS':([8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,114,116,117,118,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,],[13,14,15,16,-13,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,-97,114,116,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,117,-93,-94,-95,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,119,-97,-97,-33,-96,-97,-70,-72,-73,-74,-75,-76,-97,140,-97,142,143,-97,-91,-97,-71,-90,150,-85,-87,-82,151,-89,-78,-97,-92,154,155,-86,-88,-81,-77,156,-97,-84,-80,-79,158,-83,]),'DOCUMENTATION':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[39,39,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,39,39,-33,39,-70,-72,-73,-74,-75,-76,39,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'SUITE_SETUP':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[40,40,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,40,40,-33,40,-70,-72,-73,-74,-75,-76,40,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'SUITE_TEARDOWN':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[41,41,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,41,41,-33,41,-70,-72,-73,-74,-75,-76,41,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'METADATA':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[42,42,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,42,42,-33,42,-70,-72,-73,-74,-75,-76,42,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TEST_SETUP':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[43,43,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,43,43,-33,43,-70,-72,-73,-74,-75,-76,43,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TEST_TEARDOWN':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[44,44,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,44,44,-33,44,-70,-72,-73,-74,-75,-76,44,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TEST_TEMPLATE':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[45,45,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,45,45,-33,45,-70,-72,-73,-74,-75,-76,45,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TEST_TIMEOUT':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[46,46,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,46,46,-33,46,-70,-72,-73,-74,-75,-76,46,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'FORCE_TAGS':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[47,47,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,47,47,-33,47,-70,-72,-73,-74,-75,-76,47,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'DEFAULT_TAGS':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[48,48,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,48,48,-33,48,-70,-72,-73,-74,-75,-76,48,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'LIBRARY':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[49,49,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,49,49,-33,49,-70,-72,-73,-74,-75,-76,49,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'RESOURCE':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[50,50,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,50,50,-33,50,-70,-72,-73,-74,-75,-76,50,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'VARIABLES':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[51,51,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,51,51,-33,51,-70,-72,-73,-74,-75,-76,51,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'SETUP':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[52,52,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,52,52,-33,52,-70,-72,-73,-74,-75,-76,52,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TEARDOWN':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[53,53,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,53,53,-33,53,-70,-72,-73,-74,-75,-76,53,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TEMPLATE':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[54,54,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,54,54,-33,54,-70,-72,-73,-74,-75,-76,54,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TIMEOUT':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[55,55,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,55,55,-33,55,-70,-72,-73,-74,-75,-76,55,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'TAGS':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[56,56,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,56,56,-33,56,-70,-72,-73,-74,-75,-76,56,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'ARGUMENTS':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[57,57,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,57,57,-33,57,-70,-72,-73,-74,-75,-76,57,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'RETURN':([13,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[58,58,-11,-13,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,58,58,-33,58,-70,-72,-73,-74,-75,-76,58,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'VARIABLE':([14,59,60,111,119,],[61,61,-55,-56,-57,]),'NAME':([15,16,19,62,63,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,113,114,115,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[64,67,-13,64,-62,67,-64,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-63,-66,-65,-68,-33,-67,-70,-72,-73,-74,-75,-76,-69,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'END':([19,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,127,134,135,136,138,139,140,142,143,148,149,150,151,154,155,156,158,],[-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,128,128,-33,128,-70,-72,-73,-74,-75,-76,137,128,-71,147,-85,-87,-82,-89,-78,-86,-88,-81,-77,-84,-80,-79,-83,]),'KEYWORD':([19,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,127,131,133,134,135,136,138,139,140,142,143,145,148,149,150,151,154,155,156,158,],[-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,129,129,-33,129,-70,-72,-73,-74,-75,-76,129,144,-91,129,-71,129,-85,-87,-82,-89,-78,-92,-86,-88,-81,-77,-84,-80,-79,-83,]),'FOR':([19,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,134,135,136,138,139,140,142,143,148,149,150,151,155,156,],[-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,132,132,-33,132,-70,-72,-73,-74,-75,-76,132,-71,-90,-85,-87,-82,-89,-78,-86,-88,-81,-77,-80,-79,]),'ASSIGN':([19,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,114,116,117,120,121,122,123,124,125,126,127,131,133,134,135,136,138,139,140,142,143,145,148,149,150,151,154,155,156,158,],[-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,133,133,-33,133,-70,-72,-73,-74,-75,-76,133,145,-91,133,-71,133,-85,-87,-82,-89,-78,-92,-86,-88,-81,-77,-84,-80,-79,-83,]),'ARGUMENT':([19,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,114,116,117,118,120,121,122,123,124,125,126,127,129,130,132,134,135,136,138,139,140,141,142,143,144,146,148,149,150,151,152,153,154,155,156,157,158,],[-13,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,118,-93,-94,-95,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,91,91,-33,-96,91,-70,-72,-73,-74,-75,-76,91,91,118,91,91,-71,91,-85,-87,-82,118,-89,-78,91,118,-86,-88,-81,-77,118,91,-84,-80,-79,118,-83,]),'FOR_SEPARATOR':([89,90,91,118,132,146,],[-93,-94,-95,-96,-97,153,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'datafile':([0,],[1,]),'sections':([0,],[2,]),'section':([0,2,],[3,12,]),'setting_section':([0,2,],[4,4,]),'variable_section':([0,2,],[5,5,]),'testcase_section':([0,2,],[6,6,]),'keyword_section':([0,2,],[7,7,]),'settings':([13,],[17,]),'setting':([13,17,114,116,120,134,],[18,68,123,123,123,123,]),'documentation_setting':([13,17,114,116,120,134,],[19,19,19,19,19,19,]),'suite_setup_setting':([13,17,114,116,120,134,],[20,20,20,20,20,20,]),'suite_teardown_setting':([13,17,114,116,120,134,],[21,21,21,21,21,21,]),'metadata_setting':([13,17,114,116,120,134,],[22,22,22,22,22,22,]),'test_setup_setting':([13,17,114,116,120,134,],[23,23,23,23,23,23,]),'test_teardown_setting':([13,17,114,116,120,134,],[24,24,24,24,24,24,]),'test_template_setting':([13,17,114,116,120,134,],[25,25,25,25,25,25,]),'test_timeout_setting':([13,17,114,116,120,134,],[26,26,26,26,26,26,]),'force_tags_setting':([13,17,114,116,120,134,],[27,27,27,27,27,27,]),'default_tags_setting':([13,17,114,116,120,134,],[28,28,28,28,28,28,]),'library_setting':([13,17,114,116,120,134,],[29,29,29,29,29,29,]),'resource_setting':([13,17,114,116,120,134,],[30,30,30,30,30,30,]),'variables_setting':([13,17,114,116,120,134,],[31,31,31,31,31,31,]),'setup_setting':([13,17,114,116,120,134,],[32,32,32,32,32,32,]),'teardown_setting':([13,17,114,116,120,134,],[33,33,33,33,33,33,]),'template_setting':([13,17,114,116,120,134,],[34,34,34,34,34,34,]),'timeout_setting':([13,17,114,116,120,134,],[35,35,35,35,35,35,]),'tags_setting':([13,17,114,116,120,134,],[36,36,36,36,36,36,]),'arguments_setting':([13,17,114,116,120,134,],[37,37,37,37,37,37,]),'return_setting':([13,17,114,116,120,134,],[38,38,38,38,38,38,]),'variables':([14,],[59,]),'variable':([14,59,],[60,111,]),'tests':([15,],[62,]),'test':([15,62,],[63,113,]),'keywords':([16,],[65,]),'keyword':([16,65,],[66,115,]),'arguments':([39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,114,116,120,127,129,132,134,136,144,153,],[88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,130,130,130,130,141,146,130,130,152,157,]),'args':([39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,114,116,120,127,129,132,134,136,144,153,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'empty_arg':([39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,114,116,120,127,129,132,134,136,144,153,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'body_items':([114,116,],[120,134,]),'body_item':([114,116,120,134,],[121,121,135,135,]),'forloop':([114,116,120,134,],[122,122,122,122,]),'step':([114,116,120,127,134,136,],[124,124,124,138,124,148,]),'templatearguments':([114,116,120,127,134,136,],[125,125,125,139,125,149,]),'invalid_forloop':([114,116,120,134,],[126,126,126,126,]),'for_header':([114,116,120,134,],[127,127,127,127,]),'assignments':([114,116,120,127,134,136,],[131,131,131,131,131,131,]),'for_body':([127,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> datafile","S'",1,None,None,None),
  ('datafile -> <empty>','datafile',0,'p_datafile','parser.py',18),
  ('datafile -> sections','datafile',1,'p_datafile','parser.py',19),
  ('sections -> section','sections',1,'p_sections','parser.py',23),
  ('sections -> sections section','sections',2,'p_sections','parser.py',24),
  ('section -> setting_section','section',1,'p_section','parser.py',28),
  ('section -> variable_section','section',1,'p_section','parser.py',29),
  ('section -> testcase_section','section',1,'p_section','parser.py',30),
  ('section -> keyword_section','section',1,'p_section','parser.py',31),
  ('setting_section -> SETTING_HEADER EOS','setting_section',2,'p_setting_section','parser.py',36),
  ('setting_section -> SETTING_HEADER EOS settings','setting_section',3,'p_setting_section','parser.py',37),
  ('settings -> setting','settings',1,'p_settings','parser.py',42),
  ('settings -> settings setting','settings',2,'p_settings','parser.py',43),
  ('setting -> documentation_setting','setting',1,'p_setting','parser.py',47),
  ('setting -> suite_setup_setting EOS','setting',2,'p_setting','parser.py',48),
  ('setting -> suite_teardown_setting EOS','setting',2,'p_setting','parser.py',49),
  ('setting -> metadata_setting EOS','setting',2,'p_setting','parser.py',50),
  ('setting -> test_setup_setting EOS','setting',2,'p_setting','parser.py',51),
  ('setting -> test_teardown_setting EOS','setting',2,'p_setting','parser.py',52),
  ('setting -> test_template_setting EOS','setting',2,'p_setting','parser.py',53),
  ('setting -> test_timeout_setting EOS','setting',2,'p_setting','parser.py',54),
  ('setting -> force_tags_setting EOS','setting',2,'p_setting','parser.py',55),
  ('setting -> default_tags_setting EOS','setting',2,'p_setting','parser.py',56),
  ('setting -> library_setting EOS','setting',2,'p_setting','parser.py',57),
  ('setting -> resource_setting EOS','setting',2,'p_setting','parser.py',58),
  ('setting -> variables_setting EOS','setting',2,'p_setting','parser.py',59),
  ('setting -> setup_setting EOS','setting',2,'p_setting','parser.py',60),
  ('setting -> teardown_setting EOS','setting',2,'p_setting','parser.py',61),
  ('setting -> template_setting EOS','setting',2,'p_setting','parser.py',62),
  ('setting -> timeout_setting EOS','setting',2,'p_setting','parser.py',63),
  ('setting -> tags_setting EOS','setting',2,'p_setting','parser.py',64),
  ('setting -> arguments_setting EOS','setting',2,'p_setting','parser.py',65),
  ('setting -> return_setting EOS','setting',2,'p_setting','parser.py',66),
  ('documentation_setting -> DOCUMENTATION arguments EOS','documentation_setting',3,'p_documentation','parser.py',70),
  ('suite_setup_setting -> SUITE_SETUP arguments','suite_setup_setting',2,'p_suite_setup','parser.py',74),
  ('suite_teardown_setting -> SUITE_TEARDOWN arguments','suite_teardown_setting',2,'p_suite_teardown','parser.py',78),
  ('metadata_setting -> METADATA arguments','metadata_setting',2,'p_metadata','parser.py',82),
  ('test_setup_setting -> TEST_SETUP arguments','test_setup_setting',2,'p_test_setup','parser.py',86),
  ('test_teardown_setting -> TEST_TEARDOWN arguments','test_teardown_setting',2,'p_test_teardown','parser.py',90),
  ('test_template_setting -> TEST_TEMPLATE arguments','test_template_setting',2,'p_test_template','parser.py',94),
  ('test_timeout_setting -> TEST_TIMEOUT arguments','test_timeout_setting',2,'p_test_timeout','parser.py',98),
  ('force_tags_setting -> FORCE_TAGS arguments','force_tags_setting',2,'p_force_tags','parser.py',102),
  ('default_tags_setting -> DEFAULT_TAGS arguments','default_tags_setting',2,'p_default_tags','parser.py',106),
  ('library_setting -> LIBRARY arguments','library_setting',2,'p_library','parser.py',110),
  ('resource_setting -> RESOURCE arguments','resource_setting',2,'p_resource','parser.py',115),
  ('variables_setting -> VARIABLES arguments','variables_setting',2,'p_variables_import','parser.py',120),
  ('setup_setting -> SETUP arguments','setup_setting',2,'p_setup','parser.py',125),
  ('teardown_setting -> TEARDOWN arguments','teardown_setting',2,'p_teardown','parser.py',129),
  ('template_setting -> TEMPLATE arguments','template_setting',2,'p_template','parser.py',133),
  ('timeout_setting -> TIMEOUT arguments','timeout_setting',2,'p_timeout','parser.py',137),
  ('tags_setting -> TAGS arguments','tags_setting',2,'p_tags','parser.py',141),
  ('arguments_setting -> ARGUMENTS arguments','arguments_setting',2,'p_arguments_setting','parser.py',145),
  ('return_setting -> RETURN arguments','return_setting',2,'p_return','parser.py',149),
  ('variable_section -> VARIABLE_HEADER EOS','variable_section',2,'p_variable_section','parser.py',153),
  ('variable_section -> VARIABLE_HEADER EOS variables','variable_section',3,'p_variable_section','parser.py',154),
  ('variables -> variable','variables',1,'p_variables','parser.py',159),
  ('variables -> variables variable','variables',2,'p_variables','parser.py',160),
  ('variable -> VARIABLE arguments EOS','variable',3,'p_variable','parser.py',164),
  ('testcase_section -> TESTCASE_HEADER EOS','testcase_section',2,'p_testcase_section','parser.py',168),
  ('testcase_section -> TESTCASE_HEADER EOS tests','testcase_section',3,'p_testcase_section','parser.py',169),
  ('keyword_section -> KEYWORD_HEADER EOS','keyword_section',2,'p_keyword_section','parser.py',174),
  ('keyword_section -> KEYWORD_HEADER EOS keywords','keyword_section',3,'p_keyword_section','parser.py',175),
  ('tests -> test','tests',1,'p_tests','parser.py',180),
  ('tests -> tests test','tests',2,'p_tests','parser.py',181),
  ('keywords -> keyword','keywords',1,'p_keywords','parser.py',185),
  ('keywords -> keywords keyword','keywords',2,'p_keywords','parser.py',186),
  ('test -> NAME EOS','test',2,'p_test','parser.py',190),
  ('test -> NAME EOS body_items','test',3,'p_test','parser.py',191),
  ('keyword -> NAME EOS','keyword',2,'p_keyword','parser.py',198),
  ('keyword -> NAME EOS body_items','keyword',3,'p_keyword','parser.py',199),
  ('body_items -> body_item','body_items',1,'p_body_items','parser.py',206),
  ('body_items -> body_items body_item','body_items',2,'p_body_items','parser.py',207),
  ('body_item -> forloop','body_item',1,'p_body_item','parser.py',212),
  ('body_item -> setting','body_item',1,'p_body_item','parser.py',213),
  ('body_item -> step','body_item',1,'p_body_item','parser.py',214),
  ('body_item -> templatearguments','body_item',1,'p_body_item','parser.py',215),
  ('body_item -> invalid_forloop','body_item',1,'p_body_item','parser.py',216),
  ('step -> KEYWORD arguments EOS','step',3,'p_step','parser.py',221),
  ('step -> assignments EOS','step',2,'p_step_with_assignment','parser.py',225),
  ('step -> assignments KEYWORD arguments EOS','step',4,'p_step_with_assignment','parser.py',226),
  ('forloop -> for_header for_body END EOS','forloop',4,'p_forloop','parser.py',233),
  ('forloop -> for_header END EOS','forloop',3,'p_forloop','parser.py',234),
  ('forloop -> END EOS','forloop',2,'p_forloop','parser.py',235),
  ('for_header -> FOR arguments FOR_SEPARATOR arguments EOS','for_header',5,'p_for_header','parser.py',243),
  ('for_header -> FOR arguments EOS','for_header',3,'p_for_header','parser.py',244),
  ('for_body -> step','for_body',1,'p_for_body','parser.py',251),
  ('for_body -> for_body step','for_body',2,'p_for_body','parser.py',252),
  ('for_body -> templatearguments','for_body',1,'p_for_body','parser.py',253),
  ('for_body -> for_body templatearguments','for_body',2,'p_for_body','parser.py',254),
  ('templatearguments -> arguments EOS','templatearguments',2,'p_templatearguments','parser.py',259),
  ('invalid_forloop -> for_header for_body','invalid_forloop',2,'p_invalid_for_loop','parser.py',263),
  ('assignments -> ASSIGN','assignments',1,'p_assignments','parser.py',268),
  ('assignments -> assignments ASSIGN','assignments',2,'p_assignments','parser.py',269),
  ('arguments -> args','arguments',1,'p_arguments','parser.py',273),
  ('arguments -> empty_arg','arguments',1,'p_arguments','parser.py',274),
  ('args -> ARGUMENT','args',1,'p_args','parser.py',279),
  ('args -> arguments ARGUMENT','args',2,'p_args','parser.py',280),
  ('empty_arg -> <empty>','empty_arg',0,'p_empty_arg','parser.py',284),
]
