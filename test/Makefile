# -----------
# Phenotype Prediction
# -----------
SCRIPT =	../src/phenotype_prediction.py
RUN_DIR =	./run_dir
RUN_FILES =	../data/run_files
RESULTS_DIR =	$(RUN_DIR)/results
RMR =		rm -rf
GZIP =		gzip
GZIP_D =	gzip -d
MKDIR_P =	mkdir -p
DATA_DIR = ../data/spreadsheets
INPUT_DATA = $(foreach dir,$(DATA_DIR),$(wildcard $(dir)/*.gz))
INPUT_DATA_SUFFIX = $(suffix $(INPUT_DATA))


env_setup:  create_run_dir copy_run_files decompress_input_data

create_run_dir:
	$(MKDIR_P)  $(RESULTS_DIR)

copy_run_files:
	cp $(RUN_FILES)/*.yml $(RUN_DIR)

decompress_input_data:
	@echo Decompress input data...
ifeq ($(filter-out .gz, $(INPUT_DATA_SUFFIX)),)
	$(GZIP_D) $(INPUT_DATA)
else
	@echo No gzip file needs to be decompressed.
endif	
 

# Benchmark tests
run_elastic_net:
	python3 $(SCRIPT) -run_directory $(RUN_DIR) -run_file BENCHMARK_2_ElasticNet.yml
run_lasso:
	python3 $(SCRIPT) -run_directory $(RUN_DIR) -run_file BENCHMARK_1_Lasso.yml

# Cleanup
final_clean:	clean_dir_recursively

clean_dir_recursively:
	$(RMR) $(RUN_DIR)
#Verifying
verification_tests:
	python3 ./integration/verify_benchmarks.py
