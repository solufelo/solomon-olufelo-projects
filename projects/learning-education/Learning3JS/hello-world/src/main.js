import * as THREE from 'three';
//initialize scene
const scene = new THREE.Scene();

//create a cube
const cubeGeometry = new THREE.BoxGeometry(1, 1, 1);
//create a material
const cubeMaterial = new THREE.MeshBasicMaterial({ color: "red" });
//create a mesh
const cubeMesh = new THREE.Mesh(
    cubeGeometry,
    cubeMaterial
)
//add the mesh to the scene
scene.add(cubeMesh);
//log the scene
console.log(scene);
//create a camera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
//set the camera position
camera.position.z = 5;

//initialize the renderer
const canvas = document.querySelector(".threejs-canvas");
const renderer = new THREE.WebGLRenderer({ canvas });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.render(scene, camera);