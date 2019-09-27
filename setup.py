from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        use_scm_version=True,
        packages=find_packages(),
        include_package_data=True,
        setup_requires=[
            'setuptools_scm',
        ],
        install_requires=[],
        entry_points={
            'lying.register': [
                'wait=lying.render.common:WaitRender',
                'txt=lying.render.common:TextRender',
                'txt-status=lying.render.common:TextStatusRender',
                'cmd=lying.render.common:CmdRender',
                'input=lying.render.common:InputRender',
            ],
            'console_scripts': [
                'lying=lying.cli:main',
            ]
        }
    )
