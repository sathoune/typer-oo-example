import click


class command:
    def __init__(self, name=None, cls=click.Command, **attrs):
        self.name = name
        self.cls = cls
        self.attrs = attrs

    def __call__(self, method):
        def __command__(this):
            def wrapper(*args, **kwargs):
                return method(this, *args, **kwargs)

            if hasattr(method, "__options__"):
                options = method.__options__
            return self.cls(self.name, callback=wrapper, params=options, **self.attrs)

        method.__command__ = __command__
        return method


class option:
    def __init__(self, *param_decls, **attrs):
        self.param_decls = param_decls
        self.attrs = attrs

    def __call__(self, method):
        if not hasattr(method, "__options__"):
            method.__options__ = []

        method.__options__.append(
            click.Option(param_decls=self.param_decls, **self.attrs)
        )
        return method


class Cli:
    def __new__(cls, *args, **kwargs):
        self = super(Cli, cls).__new__(cls, *args, **kwargs)
        self._cli = click.Group()

        # Wrap instance options
        self.__option_callbacks__ = set()
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if hasattr(attr, "__options__") and not hasattr(attr, "__command__"):
                self._cli.params.extend(attr.__options__)
                self.__option_callbacks__.add(attr)

        # Wrap commands
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if hasattr(attr, "__command__"):
                command = attr.__command__(self)
                # command.params.extend(_options)
                self._cli.add_command(command)

        return self

    def run(self):
        """Run the CLI application."""
        self()

    def __call__(self):
        """Run the CLI application."""
        self._cli()