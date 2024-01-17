import * as model from "./model.js";
import recipeView from "./views/recipeViews.js";

import "core-js/stable";
import "regenerator-runtime/runtime";

const recipeContainer = document.querySelector(".recipe");

///////////////////////////////////////
console.log("Hello");

const controlRecipes = async function () {
  try {
    let id = window.location.hash.slice(1);
    console.log(id);

    if (!id) return;
    recipeView.renderSpinner();

    // 1 Loading recipe
    await model.loadRecipe(id);

    // 2 Rendering recipe
    recipeView.render(model.state.recipe);
  } catch (err) {
    console.log(err);
    recipeView.renderError();
  }
};

const init = function () {
  recipeView.addHandlerRender(controlRecipes);
};
init();
