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

env_setup:  create_run_dir copy_run_files

create_run_dir:
	$(MKDIR_P)  $(RESULTS_DIR)

copy_run_files:
	cp $(RUN_FILES)/*.yml $(RUN_DIR)

# Benchmark tests
run_elastic_net:
	python3 $(SCRIPT) -run_directory $(RUN_DIR) -run_file BENCHMARK_2_ElasticNet.yml

# Cleanup
final_clean:    clean_dir_recursively

clean_dir_recursively:
	$(RMR) $(RUN_DIR)
