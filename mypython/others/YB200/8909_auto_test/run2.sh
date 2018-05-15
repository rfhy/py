for file in $(ls *.mp4)
do
	eval am startservice -a com.roobo.autotest.start_test --es file_path "$(pwd)/${file}"
done