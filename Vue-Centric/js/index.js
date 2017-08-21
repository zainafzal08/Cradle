Vue.component('nav-elem', {
	props: ['page'],
	template: `<a class="nav-link" v-bind:style="[navElemStyle,{backgroundColor: this.backColor}]" v-on:mouseover="trigger" v-on:mouseout="untrigger">
					{{ page.title }}
				</a>`,
	data: function(){
		return {
			navElemStyle: {
				color: "#EBEBEB",
				borderLeftStyle: "solid",
				borderLeftWidth: "5px",
				borderLeftColor: this.page.col
			},
			backColor: ""
		};
	},
	methods: {
		trigger: function(){
			this.backColor = this.page.col;
		},
		untrigger: function(){
			this.backColor = "";
		}
	}
});

Vue.component('app-nav', {
	props: ['pages','course'],
	template: `<ul class="nav flex-column" v-bind:style="navStyle">
					<li class="nav-item">
						<a class="navbar-brand" v-bind:style="navBrandStyle">{{course}}</a>
					</li>
					<li class="nav-item" v-for="page in pages">
						<nav-elem v-bind:page="page"></nav-elem>
					</li>
				</ul>`,
	data: function(){
		return {
			navStyle: {
				backgroundColor: "#1a1a1a",
				width: "15%",
				height: "100vh"
			},
			navBrandStyle: {
				color: "white",
				fontSize: "1.5em",
				paddingLeft: "5%",
				paddingBottom: "10%",
				paddingTop: "5%"
			}
		}
	}
});

var app = new Vue({
	el: '#app',
	data: {
		course: "COMP1111",
		pages: [
			{id: "page_1", title: "Labs", col:"#d62c1a"},
			{id: "page_2",title: "Lectures", col:"#2077b2"}
		]
	}
});