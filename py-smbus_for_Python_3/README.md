* Download i2c-tools source archive, for example [i2c-tools_3.1.1.orig.tar.bz2](http://ftp.de.debian.org/debian/pool/main/i/i2c-tools/i2c-tools_3.1.1.orig.tar.bz2) from [Debian - Package: python-smbus](https://packages.debian.org/sid/python-smbus)

* Untar the archive and replace <tt>i2c-tools-3.1.1/py-smbus/smbusmodule.c</tt> by Bernhard Renz's version provided here. It was originally found here: [Howto compile py-smbus with python 3.2](http://www.spinics.net/lists/linux-i2c/msg08427.html).

* Install necessay packages :
```
apt-get install linux-libc-dev python3-dev
```

* Compile the module :
```
make EXTRA="py-smbus" PYTHON=python3
```

* Install the module :
```
cd py-smbus
sudo python3 setup.py install
```

* Et voilà !
```
sudo python3 test_smbus_python3.py
```

