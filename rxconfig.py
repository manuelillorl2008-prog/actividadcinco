import reflex as rx

config = rx.Config(
    app_name="jive",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)