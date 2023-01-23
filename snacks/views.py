from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://m.media-amazon.com/images/I/71UmNRQQQ6L.jpg",
                "title": "Flamin Hot Cheetos Limon",
                "description": "The limón flavor is acidic, but partners with the spice well; it's definitely not as sour as other hot chips on the market (specifically Takis Feugo). Even so, the lime flavor is prominent—this chip feels like it's equal parts salty, spicy, and sour.",
                "reference_url": "https://www.amazon.com/Cheetos-Flamin-Limon-Crunchy-Flaming/dp/B0152V95BQ"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/LD-Oatmeal-Creme-Pies.jpg/1600px-LD-Oatmeal-Creme-Pies.jpg",
                "title": "Little Debbies Oatmeal Creme Pies",
                "description": "From a recipe standpoint, the sweet treats are made with cinnamon, nutmeg, and a hint of molasses, with each bite aiming to deliver the sweet, vanilla creme flavor",
                "reference_url": "https://en.wikipedia.org/wiki/Oatmeal_Creme_Pie"
            }, {
                "image_url": "https://images.heb.com/is/image/HEBGrocery/000720417?fit=constrain,1&wid=800&hei=800&fmt=jpg&qlt=85,0&resMode=sharp2&op_usm=1.75,0.3,2,0",
                "title": "Wasabi and Soy Almonds",
                "description": "These feature the sharp distinctive sting of wasabi paired with the salty tang of soy sauce. The flavor is heavy enough to let you know it's wasabi, but not so much that it clears your sinuses or brings tears to your eyes. It's a familiar combination if you like to eat sushi and pretty addicting to boot.",
                "reference_url": "https://www.bluediamond.com/brand/snack-almonds/bold-flavors/wasabi-and-soy-sauce#:~:text=When%20we%20first%20heard%20the,with%20a%20salty%2C%20sweet%20finish."
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
