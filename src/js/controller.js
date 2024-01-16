import * as model from "./model.js";
import recipeView from "./views/recipeViews.js";

import "core-js/stable";
import "regenerator-runtime/runtime";

const recipeContainer = document.querySelector(".recipe");

const timeout = function (s) {
  return new Promise(function (_, reject) {
    setTimeout(function () {
      reject(new Error(`Request took too long! Timeout after ${s} second`));
    }, s * 1000);
  });
};

// https://forkify-api.herokuapp.com/v2

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
    alert(err);
  }
};

// controlRecipes();
// this single line replaces the two below
["hashchange", "load"].forEach((ev) =>
  window.addEventListener(ev, controlRecipes)
);
// window.addEventListener("hashchange", controlRecipes);
// window.addEventListener("load", controlRecipes);
