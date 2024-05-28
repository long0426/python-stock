FROM vhiveease/python-slim

RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh \
&& apt-get update \
&& apt-get upgrade -y \
&& apt-get -y install git openssh-server \
&& git clone https://github.com/long0426/python-stock.git \
&& pip install --upgrade pip \
&& pip install twstock \
&& pip install pandas \
&& pip install plotly \
&& pip install nbformat \
&& pip install lxml \
&& pip install BeautifulSoup4 \
&& apt-get install -y gcc python3-dev \
&& pip install ipykernel -U --user --force-reinstall \
&& mkdir /var/run/sshd \
&& chmod 0755 /var/run/sshd \
&& sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config \
&& sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

COPY id_rsa.pub /root/.ssh/authorized_keys

WORKDIR /python-stock

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]