source contrib/tf_serving/venv_tfs_nima/bin/activate \
&& python3 -W ignore -m contrib.tf_serving.tfs_sample_client \
--image-path=/var/www/RJI-Software-Engineering-Project/pictures/rji.augurlabs.io/20170902_MuMsu/1q/20170921_mumsu_mp_1399.JPG \
--model-name=mobilenet_technical